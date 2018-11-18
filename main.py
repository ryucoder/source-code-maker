from pprint import pprint
from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero, Comments

from django.views.generic import CreateView
from django.views.generic.dates import DateMixin

from django.http import HttpResponse

import pyclbr



def main():
    print()
    # source = SourceCodeMaker(Hero)
    source = SourceCodeMaker(Hero, metadata=True)
    # print(source.final_source_code)     
    source.dump_source_to_current_folder()
    # pprint(source.final_source_code)
    # pprint(source.attributes)
    # print()
    # pprint(source.methods)
    # print()
    # x = pyclbr.readmodule_ex("django.utils")
    # print(x)

    # path = "type_absolute_path_of_folder_here"
    # source.dump_source_to_specific_folder(path)


if __name__ == "__main__":
    main()

# This is a typical Dynamic Programming problem. 
# Once everything is working as expected,
# refactor the code using Bottom Up DP paradigm.
