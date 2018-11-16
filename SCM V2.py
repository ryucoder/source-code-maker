from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.generic.dates import DateMixin
import inspect
from pprint import pprint
from File001 import Hero, Base, Zero, Comments


class BaseMaker(object):
    class_name = None
    mro = None
    all_attributes_and_methods = None
    attributes = None
    methods = None

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
        return "\n Methods \n"


class SCM(MethodMixin, AttributeMixin, ClassMixin):

    def __init__(self, className, metadata=False):

        if not inspect.isclass(className):
            raise Exception("SourceCodeMaker expects a class."
                            + " Provided className attribute is not a class."
                            + " It is of type " + str(type(className)))

        self.class_name = className
        self.mro = self.class_name.mro()
        self.metadata = metadata
        self.list_and_separate_attributes_and_methods()
        self.final_source_code = self._get_final_source_code()

    def _get_final_source_code(self):
        """ Main function that creates the source code of the class """

        classLine_source = self._get_class_line()
        attributes_source = self._get_all_attributes_source()
        method_source = self._get_all_methods_source()
        final_source = "\n" + classLine_source + "\n" + attributes_source + "\n" + method_source

        return final_source

# SCM(CreateView)
# SCM(Hero)

from django.views.generic import CreateView
# print(SCM(Hero).final_source_code)
# print(SCM(Hero, metadata=True).final_source_code)
print(SCM(CreateView).final_source_code)
# print(SCM(CreateView, metadata=True).final_source_code)
# print(SCM(DateMixin, metadata=True).final_source_code)
