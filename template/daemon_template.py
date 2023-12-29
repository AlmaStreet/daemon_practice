from daemon_creator.daemon import Daemon


def user_task():
    # User's specific task logic
    message = "Performing my task..."
    my_daemon.log_task_output(message)


if __name__ == "__main__":
    daemon_name = "daemon_template"
    my_daemon = Daemon(name=daemon_name, task_function=user_task)
    my_daemon.start()
