# Folder Synchronization Script

This Python script synchronizes the contents of a source folder to a replica folder at specified intervals. It ensures that the replica folder mirrors the source folder by copying new files, updating existing files, and removing files and directories that no longer exist in the source folder.

## Features

- Periodic synchronization of two folders.
- Logs all file operations (creation, copying, removal) to the console and a log file.
- Configurable synchronization interval through command line arguments.

## Requirements

- Python 3.x
- `argparse` (standard library)
- `shutil` (standard library)
- `os` (standard library)
- `logging` (standard library)

## Setup

1. **Clone the repository**:

   ```sh
   git clone git@github.com:nodus8tollens/internal-development-test-task.git
   cd ./internal-development-test-task
   ```

2. **Create and activate a virtual environment**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install any required dependencies** (if there are any additional dependencies, specify them in a `requirements.txt` file and use the following command):
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the script with the following command:

```sh
python main.py /path/to/source /path/to/replica [interval]
```
