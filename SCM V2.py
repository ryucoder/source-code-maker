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
            
                self.attributes[item.defining_class.__name__].append((item.name, item.object))
            
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

        attrs = ""
        all_attrs = {}
        parent_classes = self.mro[0:-1]

        for parent in parent_classes:
            attr_source = ""

            print(parent)
        # for parent in parent_classes:
        #     temp = ''

        #     if self.metadata:
        #         temp += '\n    # Attributes of Class ' + parent.__name__ + "\n"

        #     class_attrs = self._get_attributes_of_one_class(parent)

        #     # Required to extract multiline variables properly
        #     extracted_variables = {}
        #     last_key = ""

        #     for temp_line in class_attrs.splitlines():
        #         if temp_line.strip() != "":
        #             split = temp_line.strip().split("=")
        #             # print(split)
        #             if len(split) == 2:
        #                 last_key = split[0]
        #                 # print(last_key)
        #                 # print()
        #                 extracted_variables[last_key] = [split[1]]
        #             elif len(split) == 1:
        #                 extracted_variables[last_key].append(split[0])

        #     for key, values in extracted_variables.items():
        #         values_source = ""
        #         values_source += values[0] + "\n"

        #         for line in values[1:]:
        #             values_source += "        " + line + "\n"

        #         variable = key + " = " + values_source

        #         if key not in all_attrs:
        #             all_attrs[key] = values

        #             if key.strip().startswith("#"):
        #                 if self.metadata:
        #                     temp += "\n    # " + "This attribute was commented."
        #                     temp += "\n    " + variable
        #             else:
        #                 temp += "    " + variable
        #                 # temp += "\n    " + variable
        #         else:
        #             if self.metadata:
        #                 temp += "\n    # Overwritten\n"
        #                 for line in variable.splitlines():
        #                     temp += "    # " + line + "\n"

        #    # if temp is empty string i.e. class does not have any attributes defined
        #     # don't add an extra empty line
        #     # if temp != "":
        #     #     temp += "\n"

        #     if self.metadata:
        #         if class_attrs.strip() == "" or class_attrs.strip() == "\n":
        #             temp += "    # No attributes are defined inside this class" + "\n"
        #     else:
        #         if temp != "":
        #             temp += "\n"

        #     attrs += temp

        # self.attributes_source_code = attrs

        # return attrs

        return "\n Attributes \n"


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
        
        final_source = "\n" + classLine_source 
                        + "\n" + attributes_source 
                        + "\n" + method_source

        return final_source

# SCM(CreateView)
# SCM(Hero)


# print(SCM(Hero, metadata=True).final_source_code)
print(SCM(DateMixin, metadata=True).final_source_code)
