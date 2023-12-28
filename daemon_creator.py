import sys
import os

OUTPUT_DIR = os.path.expanduser("~/repos/daemon_practice")


def create_daemon(caller_tag):
    # Fork the process to create a new child process
    pid = os.fork()
    if pid > 0:
        # Exit the parent process
        sys.exit()

    # Change the working directory to a safe location
    os.chdir(OUTPUT_DIR)

    # Create a new session
    os.setsid()

    # Fork again to make sure the daemon is not a session leader
    pid = os.fork()
    if pid > 0:
        sys.exit()

    # After daemon is created, log the PID
    with open(os.path.join(OUTPUT_DIR, "daemon_pid.txt"), "a") as pid_file:
        pid_file.write(f"Daemon PID: {os.getpid()}, Caller: {caller_tag}\n")
