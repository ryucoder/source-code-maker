from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base


def main():
    source = SourceCodeMaker(Hero)
    print(source.final_source_code)
    
    # source2 = SourceCodeMaker(Base)
    # print(source2.final_source_code)

    # individual working properly
    # both not working properly


if __name__ == "__main__":
    main()
    
    # get source of super methods from mro if super is called in any methods



