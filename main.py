from pprint import pprint
from SourceCodeMaker import SourceCodeMaker
from File001 import Hero, Base, Zero, Comments
from django.views.generic import TemplateView, CreateView

def main():
    print()
    # source = SourceCodeMaker(Hero, metadata=True)
    # source = SourceCodeMaker(Hero)
    source = SourceCodeMaker(CreateView, metadata=True)
    # source = SourceCodeMaker(CreateView)
    print(source.final_source_code)
    pprint(source.methods)
    pprint(source.methods_source_code)
    

if __name__ == "__main__":
    main()

# This is a typical Dynamic Programming problem. 
# Once everything is working as expected,
# refactor the code using Bottom Up DP paradigm.
