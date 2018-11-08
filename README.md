# SourceCodeMaker
SourceCodeMaker solves a real life problem of every python developer on the planet <br>
i.e. getting the Final Source Code of a Python Class that was extended from multiple classes. 

Class Based Views in Django are very hard to understand, as the class is being extended from many different classes and mixins. 
As the source code is scattered across multiple different python files and classes, understanding them can be very tricky 
and time consuming. Because none can see the final source code of the CBV in one single place. 
It becomes even messier because of the super() in python :dizzy_face:. Debugging is a real pain :joy:.

My code makes it super duper easy to get the final source code of a python class that is extended from multiple classes.
Just give a call the constructor of a SourceCodeMaker and the source code is available as an attribute. 
All of above problems are solved with just one line of code 😎.

That's not it, it takes it even further. Send kwarg metadata=True to SourceCodeMaker class and added information like MRO, which attributes and methods belongs to which class are also shown :metal: :clap: :+1:.
