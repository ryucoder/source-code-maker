from pprint import pprint
from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero, Comments

from django.views.generic import CreateView
# from django.views.generic.dates import DateMixin
# from django.http import HttpResponse


def main():
    print()
    # source = SourceCodeMaker(Hero)

    source = SourceCodeMaker(CreateView)
    # source = SourceCodeMaker(CreateView, metadata=True)
    source.ds2cf()

    # path = "type_absolute_path_of_folder_here"
    # source.dump_source_to_specific_folder(path)


if __name__ == "__main__":
    main()

# This is a typical Dynamic Programming problem. 
# Once everything is working as expected,
# refactor the code using Bottom Up DP paradigm.
