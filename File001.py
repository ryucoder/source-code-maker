""" 
Purpose: This file is the basic example of the test data classes that will be 
used to show the output of the SourceCodeMaker.

"""

class Base:
    name = "Default-Name"
    items = [1,2,'3',4,
    5,6,7,8,9]
    test = any([1,2,3])

    @classmethod
    def main():
        print("Base Main")

    def mainz():
        print("Base Mainz")


class Hero(Base):
    age = 30

    @classmethod
    def main(self):
        print("Hero Main")
