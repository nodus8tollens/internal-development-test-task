import argparse
import time
from sync import sync_folders

def main():
    parser = argparse.ArgumentParser(description="Synchronize source and replica folders.")
    parser.add_argument("source_folder", type=str, help="The source folder path")
    parser.add_argument("replica_folder", type=str, help="The replica folder path")
    parser.add_argument("interval", type=int, help="Time interval for synchronization expressed in seconds")

    args = parser.parse_args()

    source_folder = args.source_folder
    replica_folder = args.replica_folder
    interval = args.interval

    while True:
        sync_folders(source=source_folder, replica=replica_folder)
        time.sleep(interval)


if __name__ == "__main__":
    main()