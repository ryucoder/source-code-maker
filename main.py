
from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero, Comments


def main():
    print()
    source = SourceCodeMaker(Hero)
    print(source.final_source_code)
    

if __name__ == "__main__":
    main()
    # get source of super methods from mro if super is called in any methods



