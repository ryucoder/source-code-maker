
class Hero(Zero):

    items  =  ""

    age  =  30

    lifetime  =  "100 years"


    test  =  ""

    name  =  [123,
        123,123,12,3,123,123]


    def hero(self):
        print("Base hero")

    def hero(self):
        print("Hero hero")
        super(Hero, self).hero()

    @classmethod
    def main(klass):
        print("Base Main")
        super(Main, self).main()

    def main(klass):
        print("Zero Main")
        super(Zero, self).main()

    @classmethod
    def main(self):
        print("Hero Main")
        super(Hero, self).main()

    def get_lifetime(self):
        print('from zero')
        return self.lifetime

    def zero(self):
        print("Zero zero")

    def base(self):
        print("Base base")

    def mainz(self):
        print("Base Mainz")

