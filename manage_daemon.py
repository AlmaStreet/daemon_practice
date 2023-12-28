# manage_daemon.py
import os
import signal
import sys
from daemon_creator.daemon import Daemon


def list_daemons():
    daemon_files = [f for f in os.listdir(Daemon.PIDS_DIR) if f.endswith("_pid.txt")]
    return {i + 1: f[:-8] for i, f in enumerate(daemon_files)}


def stop_daemon(daemon_name):
    pid_file_path = os.path.join(Daemon.PIDS_DIR, f"{daemon_name}_pid.txt")
    try:
        with open(pid_file_path, "r") as pid_file:
            pid = int(pid_file.read().strip())
        os.kill(pid, signal.SIGTERM)
        os.remove(pid_file_path)
        print(f"Stopped daemon '{daemon_name}' with PID {pid}.")
    except Exception as e:
        print(f"Error stopping daemon '{daemon_name}': {e}")


def main():
    daemons = list_daemons()
    if not daemons:
        print("No daemons are currently running.")
        return

    for key, value in daemons.items():
        print(f"{key}) {value}")

    choice = input("Select a daemon to stop (or 0 to stop all): ")
    try:
        choice = int(choice)
        if choice == 0:
            for daemon in daemons.values():
                stop_daemon(daemon)
        elif choice in daemons:
            stop_daemon(daemons[choice])
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
