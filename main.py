from sync import sync_folders

def main():
    source_folder = "./source"
    replica_folder = "./replica"
    sync_folders(source=source_folder, replica=replica_folder)


if __name__ == "__main__":
    main()