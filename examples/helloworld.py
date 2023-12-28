from daemon_creator.daemon import Daemon


def my_custom_task():
    message = "Hello, World!"
    my_daemon.log_task_output(message)


if __name__ == "__main__":
    daemon_name = "hello_world"
    my_daemon = Daemon(name=daemon_name, task_function=my_custom_task)
    my_daemon.start()
