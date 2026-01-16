import os

current_directory = input("Please enter the directory path: ")
if not os.path.isdir(current_directory):
    print("The provided path is not a valid directory.")
    exit(1)
print(current_directory)
print("----------------FILES-------------------------")
if os.path.isfile(current_directory):
    print("The provided path is a file, not a directory.")
    exit(1)

files = os.listdir(current_directory)
files_list = [f for f in files if os.path.isfile(os.path.join(current_directory, f))]
print("Total files found:", len(files_list))
for file_name in files_list:
        if os.path.isfile(os.path.join(current_directory, file_name)):
            print("|File|: " + file_name + "     |File Size|: " + str(os.path.getsize(os.path.join(current_directory, file_name)) / 1024) + "KB")
        else:
           print("No files found in the directory.")
print("----------------FOLDERS----------------------=")
folders = [f for f in files if os.path.isdir(os.path.join(current_directory, f))]
print("Total folders found:", len(folders))
folders_files = [f for f in folders if os.path.isdir(os.path.join(current_directory, f))]
indexNumber = 1
for f in folders:
    print("Folder: " + str(indexNumber) + ") " + f)
    indexNumber += 1
for folder_name in folders:
    folder_path = os.path.join(current_directory, folder_name)
    folder_contents = os.listdir(folder_path)
    print("Contents of folder", folder_name, ":", folder_contents)
print("Total files in the folder:", len(folders_files))
if indexNumber == 1:
    print("No folders found in the directory.")
    print("----------------------------------------------")
else:
    print("do u wish to see the contents of a specific folder? (yes/no)")
    user_response = input()
    if user_response.lower() == "yes":
        print("Please enter the folder number")
    specific_folder = input()
    for f in folders:
        if specific_folder.isdigit() and int(specific_folder) == folders.index(f) + 1:
            folder_path = os.path.join(current_directory, f)
            folder_contents = os.listdir(folder_path)
            print("Contents of folder", f, ":", folder_contents)
            print("Total items in the folder:", len(folder_contents))
            print("files and their sizes: ")
            for item in folder_contents:
                item_path = os.path.join(folder_path, item)
                if os.path.isfile(item_path):
                    file_size = os.path.getsize(item_path)
                    print("File:", item, "Size:", file_size, "bytes")
            print("total file size in the folder:")
            total_size = sum(os.path.getsize(os.path.join(folder_path, item)) for item in folder_contents if os.path.isfile(os.path.join(folder_path, item)))
            print(total_size, "bytes")
        
    else:
        print("Exiting without showing specific folder contents.")

print("Summary of the directory-------------------------------------------   -------------------")
print("Total files:", len(files))
print("Total folders:", len(folders))
print("biggest file size in the directory:" + str(max(os.path.getsize(os.path.join(current_directory, f)) for f in files)))
print("smallest file size in the directory:" + str(min(os.path.getsize(os.path.join(current_directory, f)) for f in files)))
print("---------------------------------------------------------------------------------------------")