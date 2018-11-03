import os 
import sys 
import django 
import inspect

from pprint import pprint

from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero

files = []
directories = []


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
    for one_file in files:
        print(one_file)

def main():
    print()
    # source = SourceCodeMaker(Hero)
    # print(source.final_source_code)
    
    django_path = os.path.dirname(django.__file__)

    list_files_and_folders(django_path)

    print(len(files))

    count = 0
    extensions = []
    for f in files: 
        count += 1
        parts = f.split(".")
        # print(len(parts))
        # print(len(extensions))
        # print(count)
        if count == 728:
            continue
        # if parts[-1].startswith("."):
        if parts[-1] == "py":
            extensions.append(parts)
    print(len(extensions))
    
    # pprint(set(extensions))
    # pprint(extensions)
    # print(set(extensions))
        # if count == 10:
        #     break

    # import importlib

    # x = importlib.import_module("django.shortcuts")

    # for item in inspect.getmembers(x):
    #     if not item[0].startswith("__"):
    #         # print(item)
    #         if inspect.isclass(item[1]):
    #             print(item[0])


if __name__ == "__main__":
    main()

    # get source of super methods from mro if super is called in any methods



