import os
import datetime
import shutil


# Directory consolidation
def directory_organize():
    # Debugging
    # test = False
    # Prompts for directory path
    source_folder = input("Copy/Paste Path of Directory here: ")

    # Creates list of sub-folders
    list_dir = ([x[0] for x in os.walk(source_folder)])

    # Enumerate on list_dir & create dict of contents
    content_list = {}
    for index, val in enumerate(list_dir):
        path = os.path.join(source_folder, val)
        content_list[list_dir[index]] = os.listdir(path)

    # Query name of new folder
    new_folder_name = input("New Folder Name? ")

    # Checks Date & Creates new destination folder
    current_time = datetime.datetime.now()
    destination_folder = """{}-{}-{} {}""".format(
        current_time.year,
        current_time.month,
        current_time.day,
        new_folder_name)
    create_folder(source_folder, destination_folder)
    destination_path = os.path.join(source_folder, destination_folder)

    _q = True
    file = "all"
    while _q:
        # Query file type
        _file_type = input(""" Filetype?
            a - All
            b - Photos (.jpg)
            c - Videos (.mp4)
        """)
        if _file_type == "b":
            file = ".jpg"
            _q = False
        elif _file_type == "c":
            file = ".mp4"
            _q = False
        elif _file_type == "a":
            file = "all"
            _q = False
        else:
            print("Invalid Option, Try Again")

    # Loop through the list of folders
    for sub_dir in content_list:

        # Loop through the contents
        for contents in content_list[sub_dir]:

            # Make the path of the content to move
            _path = sub_dir + "/" + contents

            # Make the path with the source folder
            content_path = os.path.join(source_folder, _path)

            # Copy files with desired extension
            if not file == "all":
                if file == ".jpg" and contents.endswith(file):
                    copy_file(content_path, destination_path)
                elif file == ".mp4" and contents.endswith(file):
                    copy_file(content_path, destination_path)
            elif file == "all":
                copy_file(content_path, destination_path)

    # Debugging
    # if test:
    #     print(f"""
    #         \t===DEBUG===
    #         - Directory Path (Input)    | {source_folder}
    #         - List of Sub-folders       | {list_dir}
    #         - List of Content           | {content_list}
    #         - New Folder Name (Input)   | {destination_folder}
    #         - New Folder Path           | {destination_path}
    #         - Querying?                 | {_q}
    #         - Filetype Chosen (Input)   | {file}
    #     """)


# method to create new folder
def create_folder(parent_folder, folder_name):

    # Path
    path = os.path.join(parent_folder, folder_name)

    # Creates 'new_folder' in parent_folder
    try:
        # mode of the folder
        mode = 0o777

        # Create folder
        os.mkdir(path, mode)
    except OSError:
        print("Merging into existing folder...")
        pass


def copy_file(path_from, path_to):
    try:
        # copy the file to destination folder
        shutil.copy(path_from, path_to)
    except OSError:
        # print("Similar File exists", path_to)
        pass


directory_organize()
