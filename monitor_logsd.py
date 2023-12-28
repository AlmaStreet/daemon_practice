import time
import daemon_creator
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        with open("daemon_log.txt", "a") as log_file:
            log_file.write(f"File {event.src_path} was created at {time.ctime()}\n")


def monitor_logs():
    # Set up the watchdog observer
    path = daemon_creator.OUTPUT_DIR
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    daemon_creator.create_daemon("monitor_logs")
    monitor_logs()
