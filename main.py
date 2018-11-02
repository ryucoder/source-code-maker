from pprint import pprint as pp 
import inspect 

import File001
from File001 import one, Hero, Base
from SourceCodeMaker import SourceCodeMaker

def get_file_name(module):
    """ Returns the file name of the module """
    return module.__file__


def main():
    source = SourceCodeMaker(Hero)
    # print(source.attributes)
    # print(source.methods)
    # print(source.attributes_and_methods)
    # print(source._get_all_methods_source())
    print(source.final_source_code)


if __name__ == "__main__":
    main()
    
    #get source of super methods from mro if super is called in any methods



