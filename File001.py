""" 
Purpose: This file is the basic example of the test data classes that will be 
used to show the output of the SourceCodeMaker.

"""

class Base:
    name = "Default-Name"

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
