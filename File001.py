""" 
Purpose: This file is the basic example of the test data classes that will be 
used to show the output of the SourceCodeMaker.

"""

class Base:
    name = "Default-Name"
    items = [1,2,'3',4,
    5,7,8,9,0,6,4564,345,34,53,45,3,45,34,
    5,6,7,8,9]
    test = any([1,2,3])
    lifetime = 5

    @classmethod
    def main(klass):
        print("Base Main")
        super(Main, self).main()

    def mainz(self):
        print("Base Mainz")

    def base(self):
        print("Base base")

    def hero(self):
        print("Base hero")
        super(Hero, self).hero()

class Zero(Base):
    test = ""
    lifetime = None
    name = [123,
    123,123,12,3,123,123]

    def main(klass):
        print("Zero Main")
        super(Zero, self).main()

    def get_lifetime(self):
        print('from zero')
        return self.lifetime
        
    def zero(self):
        print("Zero zero")

    def hero(self):
        print("Zero hero")
        super()

from django.utils.functional import cached_property

class Hero(Zero):
    items = range(9)
    age = 30
    lifetime = "100 years"
    # name = "Dragon"

    def zero():
        pass


    def main(self):
        print("Hero Main")
        super(Hero, self).main()

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
        # super(Hero, self).hero()

class Comments(object):
    """
    akjhdskjaahkjda
    """
    '''
    amshdkjahsd
    '''

    """ haskjahhkjhakjs  """
    ''' klajshalkhsajlkad '''
    
    ''''''
    """"""
    
    """  ajhksdkljhasd
    askjhdkjahsdkjhaskjd """
    ''' ahgjsdjhgasd
    askjhdlkajsd '''

    comments = "Comments of above formats will not be shown in the source code."
