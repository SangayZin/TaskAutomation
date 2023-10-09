import os
import shutil
 


# Define the source directory where your files are located
source_directory = '/home/sangay/Desktop/files'

# Define the destination directory for organizing files
organize_directory = '/home/sangay/files'

# Define the backup directory where backups will be stored
backup_directory = '/home/sangay/Backup'

def organize_files(source_dir, organize_dir):
    # Iterate through files in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Skip if it's a directory
        if os.path.isdir(source_path):
            continue

        # Get the file extension
        file_extension = filename.split('.')[-1].lower()

        # Create a folder for the file extension if it doesn't exist
        extension_folder = os.path.join(organize_dir, file_extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)

        # Move the file to the appropriate folder
        destination_path = os.path.join(extension_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved {filename} to {extension_folder}")

def backup_files(source_dir, backup_dir):
    # Create a backup folder with the current date
    backup_folder = os.path.join(backup_dir, 'backup')
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    # Copy all files from the source directory to the backup directory
    for root, _, files in os.walk(source_dir):
        for filename in files:
            source_path = os.path.join(root, filename)
            backup_path = os.path.join(backup_folder, filename)
            shutil.copy2(source_path, backup_path)
            print(f"Backed up {filename} to {backup_folder}")

if __name__ == "__main__":
    organize_files(source_directory, organize_directory)
    backup_files(source_directory, backup_directory)
    print("Your files have been organized and backed up in a backup folder")
