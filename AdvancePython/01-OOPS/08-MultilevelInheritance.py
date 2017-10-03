# Multilevel Inheritance
class Car:

    def __init__(self):
        self.speed = 350
        self.tyre = 4
        self.engine = '2000cc'
        self.color = 'red'
        self.gearSystem = 'automatic'

    def showFeatures(self):
        print("Car Details :",self.speed,self.tyre,self.engine,self.color,self.gearSystem)

    def carInfo(self):
        print("Initial Car Details :",self.speed,self.tyre,self.engine,self.color,self.gearSystem)


class Audi(Car):

    def __init__(self):
        super().__init__()
        self.speed = 400
        self.engine = "2500cc"
        self.color = "black"

    # Overriding function
    def showFeatures(self):
        print("Car Details Overrided :",self.speed,self.engine,self.color,self.gearSystem)


class AudiUpdated(Audi):

    def __init__(self, speed,engine):
        super().__init__()
        self.speed = speed
        self.engine = engine


    def updatedFeatures(self):
        print("Updated features :",self.speed, self.engine, self.color,self.gearSystem)


parentObj = Car()
parentObj.carInfo()

childObj = Audi()
childObj.showFeatures()

obj = AudiUpdated(450,'3000cc')
obj.updatedFeatures()
