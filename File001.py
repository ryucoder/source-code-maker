""" 
Purpose: This file is the basic example of the test data classes that will be 
used to show the output of the SourceCodeMaker.

"""

class Base:
    name = "Default-Name"
    items = [1,2,'3',4,
    5,6,7,8,9]
    test = any([1,2,3])
    lifetime = 5

    @classmethod
    def main():
        print("Base Main")

    def mainz():
        print("Base Mainz")


class Zero(Base):
    # lifetime = None

    def get_lifetime(self):
        return self.lifetime
        

class Hero(Zero):
    age = 30
    lifetime = "100 years"

    @classmethod
    def main(self):
        print("Hero Main")
