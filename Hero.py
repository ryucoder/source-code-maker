'''
****************************************
Location of the Class Hero : 
c:\users\rajkanta\desktop\projects\source code\file001.py
****************************************
'''

class Hero(Zero):

    # ************************************************************
    # Method Resolution Order of Class Hero
    # Class Hero
    # Class Zero
    # Class Base
    # Class object
    # ************************************************************


    # Attributes of Class Hero
    items  =  range(9)
    age  =  30
    lifetime  =  "100 years"

    # This attribute was commented.
    # name  =  "Dragon"

    # Attributes of Class Zero
    test  =  ""

    # Overwritten
    # lifetime  =  None
    name  =  [123,
        123,123,12,3,123,123]

    # Attributes of Class Base

    # Overwritten
    # name  =  "Default-Name"

    # Overwritten
    # items  =  [1,2,'3',4,
    #         5,7,8,9,0,6,4564,345,34,53,45,3,45,34,
    #         5,6,7,8,9]

    # Overwritten
    # test  =  any([1,2,3])

    # Overwritten
    # lifetime  =  5

    """
    Methods defined in Class Hero
    """
    @property
    def hero(self):
        print("Hero hero")
        super(Hero, self).hero()
    @hero.setter
    def hero(self, value):
        print("Hero hero")
        super(Hero, self).hero()
    @hero.deleter
    def hero(self, vars):
        print("Hero hero")
        super(Hero, self).hero()

    # Method of Class Hero
    def zero():
        pass

    """
    Methods defined in Class Zero
    """

    # Method of Class Zero
    def get_lifetime(self):
        print('from zero')
        return self.lifetime

    """
    Methods defined in Class Base
    """

    # Method of Class Base
    def base(self):
        print("Base base")

    # Method of Class Base
    def mainz(self):
        print("Base Mainz")

