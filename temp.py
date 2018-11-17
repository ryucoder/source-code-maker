import inspect
# from inspect import *
from File001 import Hero
from pprint import pprint

# print(inspect.getblock(inspect.getsource(Hero)))

# print(getsource(Hero.hero.fget))
print(inspect.getsource(Hero.main.func))
# print(getsource(Hero.hero.fdel))

# for item in dir(Hero):
#     actual_attr = getattr(Hero, item)
#     print(item, "\t")
#     print("Callable: ", callable(item))
#     if isinstance(actual_attr, property):
#         # print(actual_attr.__class__)
#         print("Property: ", isinstance(actual_attr, property))
#         # fget, gset, gdel will be None if not defined in the class definition
#         print(actual_attr.fget)
#         print(dir(actual_attr.fget))
#         print(actual_attr.fget.__code__)
#         print(actual_attr.fset)
#         print(actual_attr.fset.__code__)
#         print(actual_attr.fdel)
#         print(actual_attr.fdel.__code__)
#     print()
