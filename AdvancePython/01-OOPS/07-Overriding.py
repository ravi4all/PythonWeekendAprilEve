class Car:

    def __init__(self):
        self.speed = 350
        self.tyre = 4
        self.engine = '2000cc'
        self.color = 'red'
        self.gearSystem = 'automatic'

    def showFeatures(self):
        print("Car Details :",self.speed,self.tyre,self.engine,self.color,self.gearSystem)


class Audi(Car):

    def __init__(self,speed,engine,color):
        super().__init__()
        self.speed = speed
        self.engine = engine
        self.color = color

    # Overriding function
    def showFeatures(self):
        print("Car Details Overrided :",self.speed,self.engine,self.color,self.gearSystem)


obj = Audi(400,'3000cc','black')
obj.showFeatures()
