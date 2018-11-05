import os
import sys
import django
import inspect
import importlib

from pprint import pprint

from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero


files = []
directories = []
modules = []
classes = []

# def extract_list_of_python_files_from_files():
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

    # Required to import dates.py
    from django.conf import settings
    settings.configure()

    for item in modules:
        filename = importlib.import_module(item)

        for item in inspect.getmembers(filename):
            if not item[0].startswith("__"):
                # print(item)
                if inspect.isclass(item[1]) and not issubclass(item[1], Exception) and not issubclass( item[1], classmethod):
                    # print(item[0])
                    classes.append(item[1])
                    # print(inspect.getsource(item[1]))


def main():
    print()
    # django_path = os.path.dirname(django.__file__)

    # list_files_and_folders(django_path)

    extract_module_strings_from_files()
    extract_classes_from_modules()

    print()
    print(len(files))
    print(len(classes))
    print()

    mixins = []
    views = []
    others = []

    for klass in classes:
        if klass.__name__.endswith("Mixin"):
            mixins.append(klass)
        elif klass.__name__.endswith("View"):
            views.append(klass)
        else: 
            others.append(klass)

    print()
    print(len(mixins))
    pprint(mixins)
    print(len(views))
    pprint(views)
    print(len(others))
    pprint(others)

    # for mixin in mixins:
    #     print(mixin.__name__, len(mixin.mro()))

    # sort the mixins in ascending order or length of mro
    # sort the views in ascending order or length of mro
    # sort the others in ascending order or length of mro

    # os.remove('code_inspect.txt')
    # os.remove('code_sourcecodemaker.txt')

    # for klass in classes:    
    #     fi = open('code_inspect.txt', 'a')
    #     scm = open('code_sourcecodemaker.txt', 'a')

    #     fi.write("****************************************\n")
    #     fi.write(inspect.getsource(klass))
    #     fi.write("****************************************\n\n")

    #     scm.write("****************************************\n")
    #     scm.write(SourceCodeMaker(klass).final_source_code)
    #     scm.write("****************************************\n\n")
        
    #     fi.close()
    #     scm.close()


if __name__ == "__main__":
    main()


# Thank and share
# https://opensource.com/article/18/5/how-retrieve-source-code-python-functions
# https: // ivxenog.in/2018/02/10/dynamically-import-module-from-string-in-python/


# Needs to fix source codes of below classes in SourceCodeMaker
# TemplateResponseMixin 


# Features to add
# 1. Get source of super methods from mro if super is called in any methods
# 2. Enable metadata info i.e. if the metadata=True then show
# which functions and attributes were brought from which class


# Main Goals to achieve in Django 
# 1. Get correct source code of all the Mixins in Django
# 2. Get correct source code of all the Class Based Views in Django
