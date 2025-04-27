import os
import shutil

# Set the path you want to organize
path = input("C:/Users/abhis/OneDrive/Documents/python_file_Organizer").strip('"')

# Dictionary to map file types to folders
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Create folders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files to corresponding folders
for file in os.listdir(path):
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        moved = False

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(path, folder, file))
                moved = True
                break
        
        if not moved:
            print(f"No folder assigned for: {file}")

print("Files organized successfully!")

    