import argparse
import time
import logging
from sync import sync_folders

# Configures the logger: level (INFO), message format, and handlers (log file name, and console output)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    handlers=[logging.FileHandler("sync.log"), logging.StreamHandler()])

# Creates a logger object with the current module name (__name__ == __main__)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Synchronize source and replica folders.")
    # Adds a positional argument from the terminal
    parser.add_argument("source_folder", type=str, help="The source folder path")
    parser.add_argument("replica_folder", type=str, help="The replica folder path")
    parser.add_argument("interval", type=int, help="Time interval for synchronization expressed in seconds")

    args = parser.parse_args()

    source_folder = args.source_folder
    replica_folder = args.replica_folder
    interval = args.interval

    while True:
        sync_folders(source=source_folder, replica=replica_folder)
        # Logs a message to the log file
        logger.info(f"Periodic operation for synchronizing {replica_folder} to {source_folder}")
        time.sleep(interval)


if __name__ == "__main__":
    main()