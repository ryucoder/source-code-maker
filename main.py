from pprint import pprint
from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base


def main():
    print()
    source = SourceCodeMaker(Base)
    # print(source.final_source_code)    

    import inspect

    # class_lines = inspect.getsource(Base)
    lines = inspect.getsource(Base).splitlines()
    pprint(source.final_source_code)
    pprint(lines)
    # method_source = self._get_all_methods_source()

    # attributes_source = self._get_all_attributes_source()
    
    # print(inspect.getsource(Hero).splitlines())

if __name__ == "__main__":
    main()
    
    # get source of super methods from mro if super is called in any methods



