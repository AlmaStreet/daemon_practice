import time
from daemon_creator.daemon import Daemon
import random

RAW_DATA = "/raw_data.txt"
PROCESSED_DATA = "/processed_data.txt"
DATA_FILE_PATH = Daemon.MOCK_DATA_DIR + RAW_DATA
PROCESSED_DATA_FILE_PATH = Daemon.MOCK_DATA_DIR + PROCESSED_DATA


def my_custom_task():
    message = "Performing my task..."
    my_daemon.log_task_output(message)

    try:
        with open(DATA_FILE_PATH, "r") as file:
            data = file.read().split()

        for input_text in data:
            processed_word = process_word(input_text.strip())
            save_processed_words([processed_word])

    except Exception as e:
        error_message = f"Error in task: {str(e)}"
        my_daemon.log_task_output(error_message)


def process_word(input_text):
    delay_seconds = random.uniform(1, 5)
    time.sleep(delay_seconds)

    return {
        "input_text": input_text,
        "output_text": f"Processed: {input_text}",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }


def save_processed_words(processed_words):
    output_file_path = PROCESSED_DATA_FILE_PATH
    with open(output_file_path, "a") as file:
        for processed_word in processed_words:
            file.write(f"Processed word: {processed_word}\n")


if __name__ == "__main__":
    daemon_name = "data_processing_daemon"
    my_daemon = Daemon(name=daemon_name, task_function=my_custom_task)
    my_daemon.start()
