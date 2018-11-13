# SourceCodeMaker
SourceCodeMaker solves a real life problem of every python developer on the planet <br>
i.e. getting the Final Source Code of a Python Class that was extended from multiple classes. 

Best example of this would be Class Based Views in Django. CBV in Django are very hard to understand, as the class is being extended from many different classes and mixins. 
As the source code is scattered across multiple different python files and classes, understanding them can be very tricky 
and time consuming. Because none can see the final source code of the CBV in one single place. 
It becomes even messier because of the super() in python :dizzy_face:. Debugging is a real pain in the ass :joy:.

My code makes it super duper easy to get the final source code of a python class that is extended from multiple classes.
Just give a call the constructor of a SourceCodeMaker and the source code is available as an attribute. If a call to super() method was made, its source code is also included. All of above problems are solved with just one line of code 😎.

That's not it, it takes it even further. Send kwarg metadata=True to SourceCodeMaker constructor and added information like MRO, which attributes and methods belongs to which class are also shown. If some attributes were overwritten in a parent class that is also shown :metal: :clap: :+1:.


# Why to use it? What is the benefit of this?
It's intended to make the life of a developer little bit easy. It is most useful during the development process. <br>
Especially debugging classes that were extended from multiple classes. <br>

Just make sure to pass metadata=True to the constructor, <br> 
you will get much information that is otherwise not readily available in one single place. <br>


# How to use it?
It's damn simple. Please refer to below examples or more details. <br>

# Example No.1 :

All you have to do is import the SourceCodeMaker class and give call to its constructor <br>
and you can access the final source code of that class in the final_cource_code attribute. Tada! <br>
If call to super() was given inside a method, its source code is also shown. <br>

***** main.py *****

from SourceCodeMaker import SourceCodeMaker <br>
from django.views.generic import CreateView <br>


source = SoureCodeMaker(CreateView).final_source_code <br>
print(source) <br>



# Example No.2 :

Passing metadata=True in the constructor will show some metadata information of the class. <br>
Metadata includes the method resolution order (MRO) of the class. <br>
Metadata also includes which attributes and methods belongs to which class in the mro. <br>
If some attributes are overwritten in a parent class that is also shown in the source code. <br>
If call to super() was given inside a method, its source code is also shown. <br>

***** main.py *****

from SourceCodeMaker import SourceCodeMaker <br>
from django.views.generic import CreateView <br>


source = SoureCodeMaker(CreateView, metadata=True).final_source_code <br>



# Example No.3 :
If the main.py file was inside the desktop folder <br>
a new file would be created in that same folder with the name of the class, in this case CreateView.py <br>


***** main.py *****

from SourceCodeMaker import SourceCodeMaker <br>
from django.views.generic import CreateView <br>


source = SoureCodeMaker(CreateView).dump_source_to_current_folder() <br>



# Example No.4 :
If the main.py file was inside the desktop folder and absolute path is given, <br>
a new file would be created in the folder that you specify as the abs_path <br>

***** main.py *****

from SourceCodeMaker import SourceCodeMaker <br>
from django.views.generic import CreateView <br>


abs_path = "Type the full absolute path of a folder" <br>
source = SoureCodeMaker(CreateView).dump_source_to_specific_folder(abs_path) <br>
