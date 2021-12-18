import os


def save_folder_exists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

