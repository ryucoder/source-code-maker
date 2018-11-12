
class Hero(Zero):

    # ************************************************************
    # Method Resolution Order of Class Hero
    # Class Hero
    # Class Zero
    # Class Base
    # Class object
    # ************************************************************

    # Attributes of Class Hero
    items  =  ""

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

    # Method of Class Base
    def hero(self):
        print("Base hero")

    # Method of Class Hero
    def hero(self):
        print("Hero hero")
        super(Hero, self).hero()

    # There is no method 'main' available in the Super Class of Base

    # Method of Class Base
    @classmethod
    def main(klass):
        print("Base Main")
        super(Main, self).main()

    # Method of Class Zero
    def main(klass):
        print("Zero Main")
        super(Zero, self).main()

    # Method of Class Hero
    @classmethod
    def main(self):
        print("Hero Main")
        super(Hero, self).main()

    """
    Methods defined in Class Zero
    """

    # Method of Class Zero
    def get_lifetime(self):
        print('from zero')
        return self.lifetime

    # Method of Class Zero
    def zero(self):
        print("Zero zero")

    """
    Methods defined in Class Base
    """

    # Method of Class Base
    def base(self):
        print("Base base")

    # Method of Class Base
    def mainz(self):
        print("Base Mainz")

