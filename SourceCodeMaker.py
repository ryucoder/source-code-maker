import inspect  
import os 

from pprint import pprint 


class SourceCodeMaker(object):
    class_name = None
    mro = None
    metadata = None
    attributes = None 
    methods = None
    attributes_and_methods = None
    class_line_source_code = None 
    attributes_source_code = None 
    methods_source_code = None 
    final_source_code = None 
    ALLOWED_MAGIC_METHODS = ["__init__", "__str__", "__repr__", "__enter__", "__exit__",
                             "__get__", "__iter__", "__next__"]
                             
    def __init__(self, className, metadata=False):

        if not inspect.isclass(className):
            raise Exception("SourceCodeMaker expects a class."
                            + " Provided className attribute is not a class."
                            + " It is of type " + str(type(className)))

        self.class_name = className
        self.mro = self.class_name.mro()
        self.metadata = metadata
        self.attributes_and_methods = self._get_all_attrs_and_methods()
        self._seperate_attributes_and_methods()
        self.final_source_code = self._get_final_source_code()

    def _get_all_attrs_and_methods(self):
        """ Returns the list of attributes and methods defined inside the class """

        attrs = []
        members = inspect.getmembers(self.class_name)

        for member in members:
            if (member[0].startswith("__") != True) or (member[0] in self.ALLOWED_MAGIC_METHODS):
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
        classLine = inspect.getsource(self.class_name).splitlines()[0]
        
        if self.metadata:
            classLine += "\n"
            classLine += "\n    # ************************************************************"
            classLine += "\n    # Method Resolution Order of Class " + self.class_name.__name__
            for klass in self.class_name.mro():
                classLine += "\n    # " + "Class " +  klass.__qualname__
            classLine += "\n    # ************************************************************"
        
        self.class_line_source_code = classLine

        return classLine

    def _get_all_attributes_source(self):

        attrs = ""
        all_attrs = {}
        mro = self.class_name.mro()
        parent_classes = mro[0:-1]

        for parent in parent_classes:
            temp = ''
    
            if self.metadata:
                temp += '\n    # Attributes of Class ' + parent.__name__
    
            class_attrs = self._get_attributes_of_one_class(parent)

            # Required to extract multiline variables properly
            extracted_variables = {}
            last_key = ""
            
            for temp_line in class_attrs.splitlines():
                if temp_line.strip() != "":
                    split = temp_line.strip().split("=")
                    # print(split)
                    if len(split) == 2:
                        last_key = split[0]
                        # print(last_key)
                        # print()
                        extracted_variables[last_key] = [split[1]]
                    elif len(split) == 1:
                        extracted_variables[last_key].append(split[0])

            for key, values in extracted_variables.items():
                values_source = ""
                values_source += values[0] + "\n"

                for line in values[1:]:
                    values_source += "        " + line + "\n"
                
                variable = key + " = " + values_source

                if key not in all_attrs:
                    all_attrs[key] = values
                    
                    if key.strip().startswith("#"):
                        if self.metadata:
                            temp += "\n    # " + "This attribute was commented." 
                            temp += "\n    " + variable
                    else:
                        temp += "\n    " + variable
                else:
                    if self.metadata:
                        temp += "\n    # Overwritten\n" 
                        for line in variable.splitlines():
                            temp += "    # " + line + "\n" 


           # if temp is empty string i.e. class does not have any attributes defined
            # don't add an extra empty line
            if temp != "":
                temp += "\n"

            if self.metadata:
                if class_attrs.strip() == "" or class_attrs.strip() == "\n":
                    temp += "    # No attributes are defined inside this class" + "\n"
            
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
        is_multiline_comment_active = False
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
            if is_multiline_comment_active and (not stripped_line[-3:] in comments):
                continue

            if stripped_line[0:3] in comments and not is_multiline_comment_active:
                is_multiline_comment_active = True
                continue

            if stripped_line[-3:] in comments:
                is_multiline_comment_active = False
                continue


            if stripped_line.startswith("@") or stripped_line.startswith("def "):
                """ First condition checks if the method was decorated """
                """ Second condition checks if the declaration of first method was found """
                break

            attrs += "\n" + line

        return attrs

    def _get_all_methods_source(self):

        source = ""

        self._sort_methods_based_on_classname()

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

        self.methods_source_code = source

        return source

    def _sort_methods_based_on_classname(self):
        methods = {}

        for method in self.methods:
            klassname = method[1].__qualname__.split(".")[0]

            if klassname not in methods.keys():
                methods[klassname] = []

            methods[klassname].append(method[1])

        self.methods = methods
    
    def _check_super_and_get_combined_source(self, klass, method):

        temp_source = ""
        super_source = ""
        super_methods = []

        for cls in klass.mro()[0:-1]:
            try:
                met = getattr(cls, method.__name__)
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
                temp = "\n    # Method of Class " + method.__qualname__.split(".")[0] 
                super_source = temp + super_source

            if "super(" not in temp_source:
                break

            elif "super(" in temp_source:
                if self.metadata and (index == (length - 1)):
                    temp_source = "\n    # There is no method '" + method.__name__ + "' available in the Super Class of " + method.__qualname__.split(".")[0] + "\n" 
                    super_source = temp_source + super_source

        return super_source

    def _dump_file(self, folder_path=None, mode="w"):
        if folder_path == None:
            raise Exception("You must provide the folder_path keyword variable in _dump_file() method.")
        
        full_path = os.path.join(folder_path, self.class_name.__name__ + ".py")

        # Location of the class_name in the folder
        location = self.class_name.__module__

        source_file = open(full_path, mode)
        
        # Writing the location of the file
        source_file.write("'''" + "\n")
        source_file.write("****************************************" + "\n")
        source_file.write("Location of the Class " 
                          + self.class_name.__name__ + " : " + location + "\n")
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
            raise Exception("Something is wrong with the current path of the file.")

    def dump_source_to_specific_folder(self, folder_path=None):
        """ Takes location of a folder to store the newly created .py file """
        
        if folder_path == None:
            raise Exception("You must provide the folder_path keyword variable.")
        else:
            self._dump_file(folder_path)

    def get_raw_source(self):
        """ Returns the raw string format of the final source code of the class """
        return repr(self.final_source_code)
