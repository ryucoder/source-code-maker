# SourceCodeMaker
SourceCodeMaker solves a real life problem of every python developer on the planet <br>
i.e. getting the Final Source Code of a Python Class that was extended from multiple classes. 

Best example of this would be Class Based Views in Django. CBV in Django are very hard to understand, as the class is being extended from many different classes and mixins. 
As the source code is scattered across multiple different python files and classes, understanding them can be very tricky 
and time consuming. Because none can see the final source code of the CBV in one single place. 
It becomes even messier because of the super() in python :dizzy_face:. Debugging is a real pain in the ass :joy:.

My code makes it super duper easy to get the final source code of a python class that is extended from multiple classes.
Just give a call the constructor of a SourceCodeMaker and the source code is available as an attribute. 
All of above problems are solved with just one line of code 😎.

That's not it, it takes it even further. Send kwarg metadata=True to SourceCodeMaker constructor and added information like MRO, which attributes and methods belongs to which class are also shown :metal: :clap: :+1:.


The question now is, How to use it?

Example No.1 :
***** main.py *****

from SourceCodeMaker import SourceCodeMaker
from django.views.generic import CreateView


source = SoureCodeMaker(CreateView).final_source_code
print(source)



Example No.2 :
***** main.py *****

from SourceCodeMaker import SourceCodeMaker
from django.views.generic import CreateView


# This will show some metadata information of the class.
# Metadata includes the method resolution order (MRO) of the class.
# Metadata also includes which attributes and methods belongs to which class in the mro.
source = SoureCodeMaker(CreateView, metadata=True).final_source_code



Example No.3 :
***** main.py *****

from SourceCodeMaker import SourceCodeMaker
from django.views.generic import CreateView

# if the main.py file was inside the desktop folder
# a new file would be created in that folder with the name of the class
# in this case CreateView.py
source = SoureCodeMaker(CreateView).dump_source_to_current_folder()



Example No.4 :
***** main.py *****

from SourceCodeMaker import SourceCodeMaker
from django.views.generic import CreateView

# if the main.py file was inside the desktop folder
# a new file would be created in the folder that you specify as the abs_path 

abs_path = "Type the full absolute path of a folder"
source = SoureCodeMaker(CreateView).dump_source_to_specific_folder(abs_path)
