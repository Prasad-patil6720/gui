import logging
import datetime

current_time = datetime.datetime.now()

# Format the timestamp to include date and time
timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")

# Create a new log file with the timestamp
log_filename = f"myapp_{timestamp_str}.log"
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    filename=log_filename,  # Set the log file (optional)
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)



logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
