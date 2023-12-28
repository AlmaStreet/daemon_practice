import sys
import time
import os
import daemon_creator


def save_hello_world():
    # Redirect standard file descriptors
    sys.stdout.flush()
    sys.stderr.flush()
    with open(os.devnull, "r") as dev_null:
        os.dup2(dev_null.fileno(), sys.stdin.fileno())
    with open("daemon_output.txt", "a") as output_file:
        os.dup2(output_file.fileno(), sys.stdout.fileno())
        os.dup2(output_file.fileno(), sys.stderr.fileno())

    # Daemon logic
    while True:
        print("Hello, World!")
        time.sleep(10)


if __name__ == "__main__":
    daemon_creator.create_daemon("hello_world")
    save_hello_world()
