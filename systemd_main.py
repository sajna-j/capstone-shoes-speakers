import signal
import sys
import logging
import time
from speakers import speak

# Function to handle termination signals
def handle_exit(signum, frame):
    logging.info("Received termination signal. Exiting gracefully...")
    sys.exit(0)

# Register signal handlers for SIGTERM and SIGINT
signal.signal(signal.SIGTERM, handle_exit)
signal.signal(signal.SIGINT, handle_exit)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

try:
    while True:
        rounded_time = round(time.time())
        if (rounded_time := round(time.time())) % 10 == 0:
            logging.info(f"It's been 10 seconds: {rounded_time}!!")
            speak("10 seconds passed", vol=70)
        time.sleep(1)
except Exception as e:
    logging.warning(f"Some error occurred: {e}")

