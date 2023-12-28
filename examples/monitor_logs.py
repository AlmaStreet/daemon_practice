import time
from daemon_creator.daemon import Daemon
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


class Watcher(FileSystemEventHandler):
    def __init__(self, logs_dir):
        self.logs_dir = logs_dir

    def on_created(self, event):
        log_file_path = os.path.join(self.logs_dir, "daemon_log.txt")

        print("Logging to:", log_file_path)  # Debugging line
        with open(log_file_path, "a") as log_file:
            log_file.write(f"File {event.src_path} was created at {time.ctime()}\n")


def my_custom_task():
    message = "Performing my task..."
    my_daemon.log_task_output(message)


if __name__ == "__main__":
    daemon_name = "monitor_logs"
    my_daemon = Daemon(name=daemon_name, task_function=my_custom_task)
    my_daemon.start()

    # Set up the watchdog observer
    path = my_daemon.get_output_dir()  # Use the daemon's output directory
    logs_dir = my_daemon.LOGS_DIR  # Get the logs directory

    event_handler = Watcher(logs_dir)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
