from pprint import pprint
from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base


def main():
    print()
    source = SourceCodeMaker(Base)
    source2 = SourceCodeMaker(Hero)
    source3 = SourceCodeMaker(Hero)
    source4 = SourceCodeMaker(Base)

    print(source.final_source_code)    
    print(source2.final_source_code)    
    print(source3.final_source_code)    
    print(source4.final_source_code)    


if __name__ == "__main__":
    main()
    
    # get source of super methods from mro if super is called in any methods



