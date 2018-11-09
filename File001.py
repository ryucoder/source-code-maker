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
    def main(klass):
        print("Base Main")

    def mainz(self):
        print("Base Mainz")

    def base(self):
        print("Base base")


class Zero(Base):
    lifetime = None
    
    def get_lifetime(self):
        print('from zero')
        return self.lifetime
        
    def zero(self):
        print("Zero zero")


class Hero(Zero):
    
    age = 30
    lifetime = "100 years"

    @classmethod
    def main(self):
        print("Hero Main")
        super(Hero, self).main()

    def hero(self):
        print("Hero hero")


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
