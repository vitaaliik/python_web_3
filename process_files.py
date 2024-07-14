import os
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor

def copy_file(file_path, dest_dir):
    file_name = os.path.basename(file_path)
    ext = file_name.split('.')[-1].lower()
    target_dir = os.path.join(dest_dir, ext)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    shutil.copy2(file_path, os.path.join(target_dir, file_name))

def process_directory(source_dir, dest_dir, executor):
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            executor.submit(copy_file, file_path, dest_dir)

def main():
    if len(sys.argv) < 2:
        print("Usage: python process_files.py <source_dir> [<dest_dir>]")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    with ThreadPoolExecutor() as executor:
        process_directory(source_dir, dest_dir, executor)

if __name__ == "__main__":
    main()
