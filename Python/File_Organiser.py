import os
import shutil
from datetime import datetime

# Class to represent a file
class File:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.extension = os.path.splitext(self.name)[1].lower()

    def move(self, target_folder):
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        new_path = os.path.join(target_folder, self.name)
        shutil.move(self.path, new_path)
        print(f"Moved file: {self.name} to {target_folder}")

    def get_creation_date(self):
        return datetime.fromtimestamp(os.path.getctime(self.path))

# Class to represent a folder
class Folder:
    def __init__(self, path):
        self.path = path
        self.files = self.scan_files()

    def scan_files(self):
        # Scans the directory for all files (ignores subfolders)
        files = []
        for filename in os.listdir(self.path):
            file_path = os.path.join(self.path, filename)
            if os.path.isfile(file_path):
                files.append(File(file_path))
        return files

    def organize_by_extension(self):
        for file in self.files:
            folder_name = file.extension[1:].upper()  # Remove leading dot and make it uppercase
            folder_path = os.path.join(self.path, folder_name)
            file.move(folder_path)

    def organize_by_creation_date(self):
        for file in self.files:
            # Get year-month as folder name
            folder_name = file.get_creation_date().strftime("%Y-%m")
            folder_path = os.path.join(self.path, folder_name)
            file.move(folder_path)

# Class to manage the organizing operations
class Organizer:
    def __init__(self, root_folder):
        self.root_folder = Folder(root_folder)

    def organize_files(self, by_extension=True, by_creation_date=False):
        if by_extension:
            print("Organizing files by extension...")
            self.root_folder.organize_by_extension()
        elif by_creation_date:
            print("Organizing files by creation date...")
            self.root_folder.organize_by_creation_date()

# Example usage:
if __name__ == "__main__":
    # Set the folder path to be organized (e.g., 'C:/Users/YourName/Documents')
    root_directory = r"C:/Users/YourName/Downloads"
    
    # Create an Organizer object for the root folder
    organizer = Organizer(root_directory)
    
    # Organize files by extension or by creation date (use True/False)
    organizer.organize_files(by_extension=True)
    # Or you could choose to organize by creation date
    # organizer.organize_files(by_creation_date=True)
