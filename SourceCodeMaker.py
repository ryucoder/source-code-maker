from pprint import pprint 
import inspect  

class SourceCodeMaker(object):
    class_name = None
    attributes = [] 
    methods = []
    attributes_and_methods = None
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
            if member[0].startswith("__") != True:
                attrs.append(member)

        return attrs
    
    def _seperate_attributes_and_methods(self):
        for item in self.attributes_and_methods:
            if callable(item[1]):
                self.methods.append(item)
            else:
                self.attributes.append(item)
    
    def _get_final_source_code(self):
        """ Main function that creates the source code of the class """

        class_lines = inspect.getsource(self.class_name)
        classLine = class_lines.splitlines()[0]
        attributes_source = self._get_all_attributes_source()
        method_source = self._get_all_methods_source()
        
        return "\n" + classLine + "\n\n" + attributes_source + method_source

    def _get_all_attributes_source(self):

        attrs = ""

        for attribute in self.attributes:
            attrs += "    " + str(attribute[0]) + " = "
            
            if type(attribute[1]) == type(str()):
                attrs += '"' + str(attribute[1]) + '"'
            elif type(attribute[1]) == type(int()):
                attrs += str(attribute[1]) 

            attrs += "\n"
                    
        return attrs

    def _get_all_methods_source(self):
        
        source = ""

        for method in self.methods:
            source += "\n" + inspect.getsource(method[1]) 
        
        source += "\n"

        return source

    def get_raw_string(self):
        return repr(self.final_source_code)
