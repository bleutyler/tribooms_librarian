
import os
import hashlib
from collections import defaultdict

def find_duplicates(source_folder=os.getcwd()):
    """
    Find duplicate files in the given folder and its subfolders.
    """
    file_hashes = defaultdict(list)
    
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                file_hashes[file_hash].append(file_path)
                print(f"Processed: {file_path} and the hasH; is {file_hash}" )
            except (OSError, IOError):
                continue
    
    duplicates = {hash_val: paths for hash_val, paths in file_hashes.items() if len(paths) > 1}
    return duplicates

def main():
    folder = os.getcwd()
    duplicates = find_duplicates(folder)
    if duplicates:
        print("Duplicate files found:")
        for hash_val, paths in duplicates.items():
            print(f"Hash: {hash_val}")
            for path in paths:
                print(f"  {path}")
            print()
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main() 