import os 
import sys 
import django 
import inspect
import  importlib   

from django.views import generic
from pprint import pprint

from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero

files = []
directories = []
modules = []
classes = []


def list_files_and_folders(folder):
    for item in os.listdir(folder):
        if item != "__pycache__":
            temp_path = os.path.join(folder, item)

            if os.path.isdir(temp_path):
                directories.append(temp_path)
                list_files_and_folders(temp_path)
            elif os.path.isfile(temp_path):
                files.append(temp_path)


def extract_module_strings_from_files():
    path = 'C:\\Program Files\\Python36\\lib\\site-packages\\django\\views\\generic'
    remove = 'C:\Program Files\Python36\lib\site-packages\\'
    
    list_files_and_folders(path)

    for name in files:
        module_name = name.replace(remove, '').replace(".py", "")
        if not module_name.endswith("__init__"):
            modules.append(module_name.replace("\\", "."))


def extract_classes_from_modules():
    
    for item in modules:
        # for some reasons dates file is not being imported
        if item != "django.views.generic.dates":

            filename = importlib.import_module(item)

            for item in inspect.getmembers(filename):
                if not item[0].startswith("__"):
                    # print(item)
                    if inspect.isclass(item[1]):
                        # print(item[0])
                        classes.append(item[1])
                        # print(inspect.getsource(item[1]))

def main():
    print()
    # source = SourceCodeMaker(Hero)
    # print(source.final_source_code)
    # django_path = os.path.dirname(django.__file__)

    # list_files_and_folders(django_path)

    # print(len(files))

    # count = 0
    # extensions = []
    # for f in files: 
    #     count += 1
    #     parts = f.split(".")
    #     # print(len(parts))
    #     # print(len(extensions))
    #     # print(count)
    #     if count == 728:
    #         continue
    #     # if parts[-1].startswith("."):
    #     if parts[-1] == "py":
    #         extensions.append(parts)
    # print(len(extensions))

    extract_module_strings_from_files()
    extract_classes_from_modules()
    
    pprint(classes)
    pprint(len(classes))

if __name__ == "__main__":
    main()




    # get source of super methods from mro if super is called in any methods



