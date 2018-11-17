import os
import inspect

from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.dates import DateMixin
from pprint import pprint
from File001 import Hero, Base, Zero, Comments


class BaseMaker(object):
    class_name = None
    mro = None
    metadata = None
    all_attributes_and_methods = None
    attributes = None
    methods = None

    def __init__(self, className, metadata=False):
        if not inspect.isclass(className):
            raise Exception("SourceCodeMaker expects a class."
                            + " Provided className attribute is not a class."
                            + " It is of type " + str(type(className)))

        self.class_name = className
        self.mro = self.class_name.mro()
        self.metadata = metadata
        self.list_and_separate_attributes_and_methods()

    def list_and_separate_attributes_and_methods(self):
        """ This method does 2 things """ 
        """ 1. lists all the attributes and methods of the class """ 
        """ 2. Seperates attributes and methods based on mro"""

        self.attributes = {}
        self.methods = {}

        for item in inspect.classify_class_attrs(self.class_name):
            if item.kind == "data" and (not item.name.startswith("__")): # These are attributes
            
                if self.attributes.get(item.defining_class.__name__, None) is None:
                    self.attributes[item.defining_class.__name__] = []
            
                self.attributes[item.defining_class.__name__].append({"name": item.name, "value": item.object})
            
            elif item.kind == "method" and (item.defining_class != object): # These are methods
            
                if self.methods.get(item.defining_class.__name__, None) is None:
                    self.methods[item.defining_class.__name__] = []
            
                self.methods[item.defining_class.__name__].append((item.name, item.object))

        # self.all_attributes_and_methods = self.attributes + self.methods

    # def list_and_separate_attributes_and_methods(self):
    #     self.attributes = []
    #     self.methods = []

    #     for item in inspect.classify_class_attrs(self.class_name):
    #         if item.kind == "data" and (not item.name.startswith("__")): # These are attributes
    #             self.attributes.append((item.name, item.object, item.defining_class.__name__))
    #         elif item.kind == "method" and (item.defining_class != object): # These are methods
    #             self.methods.append((item.name, item.object))

    #     self.all_attributes_and_methods = self.attributes + self.methods


class ClassMixin(BaseMaker):

    def _get_class_line(self):
        classLine = inspect.getsource(self.class_name).splitlines()[0]

        if self.metadata:
            classLine += "\n"
            classLine += "\n    # ************************************************************"
            classLine += "\n    # Method Resolution Order of Class " + self.class_name.__name__
            for klass in self.class_name.mro():
                classLine += "\n    # " + "Class " + klass.__qualname__
            classLine += "\n    # ************************************************************"

        classLine += "\n"

        self.class_line_source_code = classLine

        return classLine


class AttributeMixin(BaseMaker):

    def _get_all_attributes_source(self):

        all_attrs_source = ""
        parent_classes = self.mro[0:-1]

        for parent in parent_classes:
            class_attr = ""

            if self.metadata:
                class_attr += '\n    # Attributes of Class ' + parent.__name__ + "\n"

            if self.attributes.get(parent.__name__, None) is not None:

                for attribute in self.attributes[parent.__name__]:
                    if attribute["value"] == "":
                        class_attr += "    " + attribute["name"] + " = " + "''" 
                    elif inspect.isclass(attribute["value"]):
                        class_attr += "    " + attribute["name"] + " = " + attribute["value"].__name__ 
                    else:
                        class_attr += "    " + attribute["name"] + " = " + str(attribute["value"]) 
                    
                    class_attr += "\n"

                all_attrs_source += class_attr + "\n"

            else:

                if self.metadata:
                    if class_attr.strip() == "# Attributes of Class " + parent.__name__:
                        class_attr += "    " + parent.__name__ + " does not have any attributes." + "\n"
                        all_attrs_source += class_attr + "\n"
                 
        return all_attrs_source


class MethodMixin(BaseMaker):

    def _get_all_methods_source(self):

        source = ""

        # self._sort_methods_based_on_classname()

        for klass in self.mro[0:-1]:

            if self.metadata:
                source += '\n    """\n'
                source += "    Methods defined in Class " + klass.__name__
                source += '\n    """\n'

            if len(self.methods.get(klass.__name__, "")) > 0:
                for method in self.methods[klass.__name__]:
                    super_source = self._check_super_and_get_combined_source(klass, method)
                    source += super_source

            else:
                if self.metadata:
                    source += "\n    # No methods are defined in Class " + klass.__name__ + "\n"

        source += "\n"

        # print()
        # print("source")
        # print(source)
        # print()

        self.methods_source_code = source

        return source


    def _check_super_and_get_combined_source(self, klass, method):

        temp_source = ""
        super_source = ""
        super_methods = []

        # This will fetch alist of methods on the super classes with the same name
        for cls in klass.mro()[0:-1]:
            try:
                met = getattr(cls, method[0])
            except AttributeError:
                met = ""

            if (met != "") and (met not in super_methods):
                super_methods.append(met)

        length = len(super_methods)

        for index, method in enumerate(super_methods):

            temp_source = ""
            temp_source = inspect.getsource(method)
            super_source = "\n" + temp_source + super_source

            if self.metadata:
                temp = "\n    # Method of Class " + \
                    method.__qualname__.split(".")[0]
                super_source = temp + super_source

            if "super(" not in temp_source:
                break

            elif "super(" in temp_source:
                if self.metadata and (index == (length - 1)):
                    temp_source = "\n    # There is no method '" + method.__name__ + \
                        "' available in the Super Class of " + \
                        method.__qualname__.split(".")[0] + "\n"
                    super_source = temp_source + super_source

        return super_source


class SCM(MethodMixin, AttributeMixin, ClassMixin):

    def __init__(self, className, metadata=False):
        super(SCM, self).__init__(className, metadata)
        self.final_source_code = self._get_final_source_code()

    def _get_final_source_code(self):
        """ Main function that creates the source code of the class """

        classLine_source = self._get_class_line()
        attributes_source = self._get_all_attributes_source()
        method_source = self._get_all_methods_source()
        final_source = "\n" + classLine_source + "\n" + attributes_source + "\n" + method_source

        return final_source

    def _dump_file(self, folder_path=None, mode="w"):
        if folder_path == None:
            raise Exception(
                "You must provide the folder_path keyword variable in _dump_file() method.")

        full_path = os.path.join(folder_path, self.class_name.__name__ + ".py")

        # Location of the class_name in the folder
        location = inspect.getabsfile(self.class_name)

        source_file = open(full_path, mode)

        # Writing the location of the file
        source_file.write("'''" + "\n")
        source_file.write("****************************************" + "\n")
        source_file.write("Location of the Class " +
                          self.class_name.__name__ + " : " + "\n")
        source_file.write(location + "\n")
        source_file.write("****************************************" + "\n")
        source_file.write("'''" + "\n")

        # Writing the final source code the file
        for line in self.final_source_code.splitlines():
            source_file.write(line + "\n")
        source_file.close()

        self._print_result(full_path)

    def _print_result(self, full_path):
        print()
        print("************************************")
        print()
        print("SourceCodeMaker Rocks!")
        print()
        print("Source Code of the class "
              + self.class_name.__name__
              + " was created successfully in below file.")
        print()
        print(full_path)
        print()
        print("************************************")
        print()

    def dump_source_to_current_folder(self, mode="w"):
        """ Creates a new file for the source code with the name of the class with .py extension """
        """ E.g. if the class name was CreateView, this method would create a new file CreateView.py """
        """ Location of this new CreateView.py file would be the folder of the file from which SourceCodeMaker was called. """

        frame = inspect.stack()[1]
        filename = frame[0].f_code.co_filename
        folder_path = os.path.dirname(filename)

        if os.path.isabs(folder_path):
            self._dump_file(folder_path, mode)
        else:
            raise Exception(
                "Something is wrong with the current path of the file.")

    def dump_source_to_specific_folder(self, folder_path=None):
        """ Takes location of a folder to store the newly created .py file """

        if folder_path == None:
            raise Exception(
                "You must provide the folder_path keyword variable.")
        else:
            self._dump_file(folder_path)

    def get_raw_source(self):
        """ Returns the raw string format of the final source code of the class """
        return repr(self.final_source_code)


from django.views.generic import CreateView
# print(SCM(Hero).final_source_code)
# print(SCM(Hero, metadata=True).final_source_code)
print(SCM(CreateView).final_source_code)
# SCM(CreateView,metadata=True).dump_source_to_current_folder()
# print(SCM(CreateView, metadata=True).final_source_code)
# print(SCM(DateMixin, metadata=True).final_source_code)
