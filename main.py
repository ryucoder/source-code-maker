from pprint import pprint
from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero


def main():
    print()
    source = SourceCodeMaker(Hero)
    source2 = SourceCodeMaker(Base).final_source_code
    print(source.final_source_code)
    print(source2)

if __name__ == "__main__":
    main()

    # get source of super methods from mro if super is called in any methods



