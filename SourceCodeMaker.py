from pprint import pprint 
import inspect  
from File001 import Hero, Base


class SourceCodeMaker(object):
    class_name = None
    attributes = None 
    methods = None
    attributes_and_methods = None
    class_line_source_code = None 
    attributes_source_code = None 
    methods_source_code = None 
    final_source_code = None 

    def __init__(self, className):

        # check if className is class or not. if not raise an error

        self.class_name = className
        self.attributes_and_methods = self._get_all_attrs_and_methods()
        self._seperate_attributes_and_methods()
        self.final_source_code = self._get_final_source_code()

    def _get_all_attrs_and_methods(self):
        """ Returns the list of attributes and methods defined inside the class """

        attrs = []
        members = inspect.getmembers(self.class_name)

        for member in members:
            if (member[0].startswith("__") != True) or (member[0] == "__init__"):
                # First condition adds all the non __name__ type variables
                # Second conditions allows the __init__ method to be added
                attrs.append(member)

        return attrs
    
    def _seperate_attributes_and_methods(self):

        self.attributes = []
        self.methods = []
        
        for item in self.attributes_and_methods:
            if callable(item[1]):
                self.methods.append(item)
            else:
                self.attributes.append(item)
            
    def _get_final_source_code(self):
        """ Main function that creates the source code of the class """

        classLine = self._get_class_line()
        attributes_source = self._get_all_attributes_source()
        method_source = self._get_all_methods_source()
        final_source = "\n" + classLine + "\n" + attributes_source + method_source

        return final_source

    def _get_class_line(self):
        # class_lines = inspect.getsource(self.class_name)
        classLine = inspect.getsource(self.class_name).splitlines()[0]
        self.class_line_source_code = classLine
        return classLine

    def _get_all_attributes_source(self):

        attrs = ""

        mro = self.class_name.mro()

        
        # if issubclass(self.class_name, Exception):
        #     parent_classes = mro[0:-3]
        # else:
        parent_classes = mro[0:-1]

        for parent in parent_classes:
            temp = ''
            temp_attrs = self._get_attributes_of_one_class(parent)

            for temp_line in temp_attrs.splitlines():
                if (temp_line.strip().split("=")[0] not in attrs) and (not temp_line.strip().startswith("#")):
                    """ First Condition checks if the variable name is in the attrs """
                    """ Second Condition makes sure that variable name is not commented """
                    temp += "\n" + temp_line
            
            # if temp is empty string i.e. class does not have any attributes defined
            # don't add an extra empty line
            if temp != "":
                temp += "\n"

            attrs += temp

        self.attributes_source_code = attrs

        return attrs

    def _get_attributes_of_one_class(self, class_name):
        """ Logic Start """
        """ After the first line, till the finding of first method, """
        """ everything is considered as attributes """
        """ Logic Ends """

        """ Only this function needs updating, rest of the code works great """

        attrs = ''
        class_lines = inspect.getsource(class_name).splitlines()[1:]
        is_multi = False
        comments = ['"""', "'''"]

        for line in class_lines:

            # print(repr(line))

            stripped_line = line.strip()

            # remove multiline comments written on a single line
            if stripped_line[0:3] in comments and stripped_line[-3:] in comments and  len(stripped_line) > 5:
                continue    

            # Don't process empty lines
            if line == "":
                continue

            # Remove single line comments here

            # dont process multiline comments
            if is_multi and (not stripped_line[-3:] in comments):
                continue

            if stripped_line[0:3] in comments and not is_multi:
                is_multi = True
                continue

            if stripped_line[-3:] in comments:
                is_multi = False
                continue


            if stripped_line.startswith("@") or stripped_line.startswith("def "):
                """ First condition checks if the method was decorated """
                """ Second condition checks if the declaration of first method was found """
                break

            attrs += "\n" + line

        return attrs

    slot_wrapper = []

    def _get_all_methods_source(self):
        
        source = ""
    
        for method in self.methods:
            if method[1] != object.__init__:
                source += "\n" + inspect.getsource(method[1]) 
        
        source += "\n"

        self.methods_source_code = source

        return source

    def get_raw_string(self):
        return repr(self.final_source_code)

    # def _get_all_attributes_source(self):
    #  """ This commented code is kept for future reference only. """
    #     attrs = ""

    #     for attribute in self.attributes:
    #         attrs += "    " + str(attribute[0]) + " = "

    #         """ This is dumb way of doing things """
    #         """ Needs a better way to do this """
    #         """ Otherwise needs to add elif causes for every new type of datatype """
    #         if type(attribute[1]) == type(str()):
    #             attrs += '"' + str(attribute[1]) + '"'
    #         elif type(attribute[1]) == type(int()):
    #             attrs += str(attribute[1])
    #         """ Quick Fix Ends Here """

    #         attrs += "\n"

    #     return attrs
