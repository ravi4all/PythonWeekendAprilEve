class Robot:
    id = 0
    def __init__(self,name):
        self.name = name
        Robot.id += 1

        print("Id",Robot.id)

        if self.name:
            print("My name is ",self.name)
        else:
            print("I do not have any name")

    def config(self):
        self.memory = "1zb"
        self.age = 100
        print("Memory : {}, Age {}".format(self.memory, self.age))

    def set_name(self):
        self.name

    def get_name(self):
        return self.name

class Robo_1(Robot):

    def __init__(self,name):
        super().__init__(name)
        self.name = name

    def build_year(self,year):
        print("I was build in",year)


class Robo_1_working(Robo_1,Robot):

    def __init__(self,name,iq):
        self.iq = iq
        super().__init__(name)
        print("My IQ is",self.iq)


# robo = Robo_1("Chitti")
# robo.config()
# robo.build_year(1917)


robo_obj = Robo_1_working("Mark","76%")
robo_obj.config()
robo_obj.build_year(1912)

