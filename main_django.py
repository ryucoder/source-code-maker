import os
import sys
import django
import inspect
import importlib
from django.views.generic import (TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView)

from pprint import pprint

from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero


files = []
directories = []
modules = []
classes = []
mixins = []
views = []
others = []


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
    django_path = os.path.dirname(django.__file__)
    remove = os.path.dirname(django_path)

    for name in files:
        # list slicing is required as the resulting module_name starts with a \
        module_name = name.replace(remove, '').replace(".py", "")[1:]

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


def extract_mixins_views_others_from_classes():
    for klass in classes:
        if klass.__name__.endswith("Mixin"):
            mixins.append(klass)
        elif klass.__name__.endswith("View"):
            views.append(klass)
        else:
            others.append(klass)


def sort_based_on_mro_count(classes):
    klass_mro_count = []
    unique_mro = []
    sorted_klasses = []

    for klass in classes:
        length = len(klass.mro())
        klass_mro_count.append((klass, length))
        if length not in unique_mro:
            unique_mro.append(length)

    for mro in sorted(unique_mro):
        for klass in klass_mro_count:
            if klass[1] == mro:
                sorted_klasses.append(klass)

    return sorted_klasses


def generate_source_CRUD():
    django_cbv = [TemplateView, CreateView, ListView,
                    DetailView, UpdateView, DeleteView]

    for view in django_cbv:
        view_source = SourceCodeMaker(view, metadata=True).final_source_code
        file_name = view.__name__ + ".txt"
        view_file = open(file_name, "w")

        for line in view_source.splitlines():
            view_file.write(line + "\n")
        
        view_file.close()


def main():
    global mixins   
    global views
    global others   

    print()

    django_path = os.path.dirname(django.__file__)
    views_path = os.path.join(django_path, "views", "generic")
   
    list_files_and_folders(views_path)
    extract_module_strings_from_files()
    extract_classes_from_modules()
    extract_mixins_views_others_from_classes()

    mixins = sort_based_on_mro_count(set(mixins))
    views = sort_based_on_mro_count(set(views))
    others = sort_based_on_mro_count(set(others))

    mixins_length = len(mixins)
    views_length = len(views)
    others_length = len(others)
    total_length = mixins_length + views_length + others_length

    print("Mixin Classes: ", mixins_length)
    print("View Classes: ", views_length)
    print("Other Classes: ", others_length)
    print("Total Classes: ", total_length)
    print()


    # Utility method to generate sources of nost common generic views in django
    # django_cbv = [TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView]
    # generate_source_CRUD()

    from django.http.response import HttpResponse
    SourceCodeMaker(CreateView).dump_source_to_current_folder(mode="w")
    # count = 0
    # for classname in others:
        # if count == 3:
            # break
        # if classname[1] == 5:
        # SourceCodeMaker(classname[0]).dump_source_to_current_folder()
        # count += 1
    # os.remove('code_inspect.txt')
    # os.remove('code_sourcecodemaker.txt')

    # for klass in mixins:
    #     if klass[1] == 3:
    #         fi = open('code_inspect.txt', 'a')
    #         scm = open('code_sourcecodemaker.txt', 'a')

    #         fi.write("****************************************\n")
    #         fi.write(inspect.getsource(klass[0]))
    #         fi.write("****************************************\n\n")

    #         scm.write("****************************************\n")
    #         scm.write(SourceCodeMaker(klass[0]).final_source_code)
    #         scm.write("****************************************\n\n")
            
    #         fi.close()
    #         scm.close()


if __name__ == "__main__":
    main()


# Thank and share
# https://opensource.com/article/18/5/how-retrieve-source-code-python-functions
# https://ivxenog.in/2018/02/10/dynamically-import-module-from-string-in-python/


# Needs to fix source codes of below classes in SourceCodeMaker
# 1. TemplateResponseMixin 
# 2. class DateMixin(object):
    # @cached_property
    # def uses_datetime_field(self):
# 3. if attributes are overwritten then below message is not shown in the metadata
# # No attributes are defined inside this class"
# instead shown below message 
# attribute name = value # this was overwritten in above class


# Features to add
# 1. Get source of super methods from mro if super is called in any methods
# 2. Enable metadata info i.e. if the metadata=True then show
# which functions and attributes were brought from which class
# print(Main.get.__qualname__)
# print(Main.turbo.__qualname__)
# 3. Method name order _name() first, name() last, sort names


# Main Goals to achieve in Django 
# 1. Get correct source code of all the Mixins in Django
# 2. Get correct source code of all the Class Based Views in Django
