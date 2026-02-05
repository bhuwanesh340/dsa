"list all the file names in folder"

import os

def list_files_in_folder(folder_path):
    try:
        # List all files and directories in the given folder
        items = os.listdir(folder_path)
        # Filter out only files
        files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]
        return files
    except FileNotFoundError:
        return f"The folder path '{folder_path}' does not exist."
    except Exception as e:
        return str(e)
    
if __name__ == "__main__":
    folder_path = r"E:\baby\selected"  # Use raw string to handle backslashes properly
    files = list_files_in_folder(folder_path)
    print("Files in folder:", files)

    files_string = ", ".join(files)
    print("Files as string:", files_string)