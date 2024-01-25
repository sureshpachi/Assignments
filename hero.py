import shutil
import sys
import time

def backup_files(source_path, dest_path):
    if not os.path.exists(source_path):
        print(f"Source directory '{source_path}' does not exist.")
        return

    if not os.path.exists(dest_path):
        print(f"destination directory '{source_path}' does not exist.")
        return

    for file_name in os.listdir(source_path):
        source_file_path = os.path.join(source_path, file_name)
        dest_file_path = os.path.join(dest_path, file_name)
try:
            shutil.copy2(source_file_path, dest_file_path)
            print(f"Copied '{source_file_path}' to '{dest_file_path}'")
        except Exception as e:
            print(f"Error occurred while copying '{source_file_path}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        A = sys.argv[1]
        B = sys.argv[2]
        backup_files(A, B)