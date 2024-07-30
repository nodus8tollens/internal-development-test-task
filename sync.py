import os
import shutil

def sync_folders(source, replica):
    # Checks if source and replica exist
    if not os.path.exists(source):
        raise ValueError(f"Source folder '{source}' does not exist.")
    if not os.path.exists(replica):
        os.makedirs(replica)
    
    # Creates a directory tree and yields a 3-tuple (root, list of subdirectories, list of files)
    # It walks through the tree of directories/subdirectories/and files
    # Repeating the further-stated imperatives for each one of them
    for root, dirs, files in os.walk(source):
        # Returns a relative path from the source folder to the root directory
        relative_path = os.path.relpath(root, source)
        # Replicates the relative paths from the source folder to the replica folder
        replica_root = os.path.join(replica, relative_path)
        
        # Ensures the replicated subdirectories exist
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
        
        # Iterates through files and copies them
        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)
            
            # Checks if a specific file doesn't exist in replica folder OR if said file has been modified
            # Performs copy (data and metadata) 
            if (not os.path.exists(replica_file) or 
                os.path.getmtime(source_file) > os.path.getmtime(replica_file)):
                shutil.copy2(source_file, replica_file)
        
        # Remove surplus files in replica that are not in source folder
        for replica_file in os.listdir(replica_root):
            replica_file_path = os.path.join(replica_root, replica_file)
            if replica_file not in files and os.path.isfile(replica_file_path):
                os.remove(replica_file_path)
    
    # Remove extra directories in replica by walking it bottom-to-top
    for root, dirs, files in os.walk(replica, topdown=False):
        for directory in dirs:
            replica_dir = os.path.join(root, directory)
            relative_path = os.path.relpath(replica_dir, replica)
            source_dir = os.path.join(source, relative_path)
            
            # If the source folder doesn't contain the conjoined relative path
            # recursivelly remove the directory in the replica folder and all of its contents
            if not os.path.exists(source_dir):
                shutil.rmtree(replica_dir)
