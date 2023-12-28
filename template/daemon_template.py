# custom_daemon.py
from daemon_creator.daemon import Daemon

def my_custom_task():
    # User's specific task logic
    # For example: perform some computation, check a condition, etc.
    # Let's assume the task creates a message string
    message = "Performing my task..."
    my_daemon.log_task_output(message)

if __name__ == "__main__":
    daemon_name = "daemon_template"
    my_daemon = Daemon(name=daemon_name, task_function=my_custom_task)
    my_daemon.start()
