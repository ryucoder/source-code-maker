



def one():
    print("One")


def two():
    print("Two")

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
