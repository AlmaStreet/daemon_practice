import configparser
import sys
import os
import logging
import signal
import time
import datetime
from logging.handlers import RotatingFileHandler


class Daemon:
    CONFIG_FILE = ".settings"
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    DEFAULT_OUTPUT_DIR = os.path.expanduser(
        config.get("DEFAULT", "output_dir", fallback="~/repos/daemon_practice")
    )

    LOGS_DIR = os.path.join(DEFAULT_OUTPUT_DIR, "logs")
    OUTPUT_DIR = os.path.join(DEFAULT_OUTPUT_DIR, "output")
    PIDS_DIR = os.path.join(DEFAULT_OUTPUT_DIR, "pids")

    DEFAULT_LOG_FILE = "daemon.log"
    LOG_FILE_MAX_SIZE = 5 * 1024 * 1024  # 5 MB
    LOG_BACKUP_COUNT = 3  # Keep 3 backup logs

    def __init__(self, name, task_function, log_level=logging.INFO, task_interval=10):
        self.name = name
        self.task_function = task_function
        self.log_level = log_level
        self.task_interval = task_interval
        self.setup_logging()

    def setup_logging(self):
        os.makedirs(self.LOGS_DIR, exist_ok=True)
        log_file = os.path.join(self.LOGS_DIR, f"{self.name}.log")
        handler = RotatingFileHandler(
            log_file,
            maxBytes=Daemon.LOG_FILE_MAX_SIZE,
            backupCount=Daemon.LOG_BACKUP_COUNT,
        )

        # Configure logging to use only the file handler, without logging to stderr
        logging.basicConfig(
            level=self.log_level, format="%(asctime)s:%(levelname)s:%(message)s"
        )
        logging.getLogger().handlers = [
            handler
        ]  # Replace default handlers with just the file handler

    def start(self):
        if self.is_already_running():
            logging.error(f"Daemon '{self.name}' is already running.")
            return
        self.create_daemon_process()
        self.configure_signal_handlers()
        self.run_loop()

    def is_already_running(self):
        pid = self.read_pid_file()
        if pid and self.is_process_running(pid):
            return True
        return False

    def create_daemon_process(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
            os.chdir(self.DEFAULT_OUTPUT_DIR)
            os.setsid()
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            logging.error(f"Error creating daemon process: {e}")
            sys.exit(1)
        self.write_pid_file()

    def configure_signal_handlers(self):
        signal.signal(signal.SIGTERM, self.signal_handler)
        signal.signal(signal.SIGHUP, self.signal_handler)

    def signal_handler(self, signum, frame):
        if signum == signal.SIGTERM:
            logging.info(f"Daemon '{self.name}' received SIGTERM signal.")
            self.cleanup()
            sys.exit(0)
        elif signum == signal.SIGHUP:
            logging.info(f"Daemon '{self.name}' received SIGHUP signal.")

    def run_loop(self):
        while True:
            self.task_function()
            time.sleep(self.task_interval)

    def write_pid_file(self):
        os.makedirs(self.PIDS_DIR, exist_ok=True)
        pid_file_path = os.path.join(self.PIDS_DIR, f"{self.name}_pid.txt")

        with open(pid_file_path, "w") as pid_file:
            pid_file.write(str(os.getpid()))

    def read_pid_file(self):
        pid_file_path = os.path.join(self.PIDS_DIR, f"{self.name}_pid.txt")
        if os.path.exists(pid_file_path):
            with open(pid_file_path, "r") as pid_file:
                return int(pid_file.read().strip())
        return None

    def log_task_output(self, message):
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_line = f"[{current_time}] {self.name} (PID: {os.getpid()}): {message}\n"
        output_file_path = os.path.join(self.OUTPUT_DIR, f"{self.name}_output.txt")

        with open(output_file_path, "a") as output_file:
            output_file.write(output_line)

    def cleanup(self):
        self.delete_pid_file()
        logging.info(f"Daemon '{self.name}' cleaned up and shutting down.")

    def delete_pid_file(self):
        pid_file_path = os.path.join(self.PIDS_DIR, f"{self.name}_pid.txt")
        if os.path.exists(pid_file_path):
            os.remove(pid_file_path)

    @staticmethod
    def is_process_running(pid):
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False

    @staticmethod
    def get_output_dir():
        return Daemon.DEFAULT_OUTPUT_DIR
