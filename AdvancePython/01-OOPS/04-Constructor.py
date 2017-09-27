class Player:
    # x = "Hello"
    # name = []
    # score = []

    def __init__(self):
        self.name = []
        self.score = []

    def show(self, n, s):
        # print(self.x)
        self.name.append(n)
        self.score.append(s)
        print("Name is {} and score is {}".format(self.name, self.score))


obj = Player()
obj.show('Sachin', 86)

obj_1 = Player()
obj_1.show('Sehwag', 65)
