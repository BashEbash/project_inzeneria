import os
from sys import platform
import urllib.request

def save_folder_exists(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

def file_size(file):
    file.seek(0, os.SEEK_END)
    file_size = file.tell()
    file.seek(0)
    return file_size

def model_exists():
    source = "https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5"
    path = "Static/AIModel/"
    if not os.path.exists(path + "resnet50_coco_best_v2.1.0.h5"):
        if platform == "linux" or platform == "linux2":
            os.system(f"wget -P {path} {source}")
        elif platform == "win32" or platform == "win64":
            urllib.request.urlretrieve(source, path + "resnet50_coco_best_v2.1.0.h5")

