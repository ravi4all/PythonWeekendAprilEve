class User_1:

    def __init__(self):
        self._userName = ''
        self.__userMail = ''
        self.__mobile = None
        self._friends = None
        self._photos = None

    def __get__(self):
        pass

    def __set__(self):
        self._userName = 'Ram'
        self.__userMail = 'ram@gmail.com'
        self.__mobile = 8978978908
        self._friends = 250
        self._photos = 112

        return self._userName, self.__userMail, self.__mobile, self._friends, self._photos


class User_2(User_1):

    def __init__(self):
        self.userName = 'Shyam'
        self.__userMail = 'shyam@gmail.com'
        self.__mobile = 9877889098
        self.friends = 412
        self.photos = 119

    def timeLine_1(self):
        print("User_1",super().__set__())

    def timeLine_2(self):
        print("User_2",self.userName, self.__userMail, self.__mobile, self.friends, self.photos)

    def show(self):
        print("User 1: ", self._userName, self._friends, self._photos)
        print("User 2: ", self.__userMail, self.__mobile)


obj = User_2()
obj.timeLine_1()
obj.timeLine_2()
obj.show()
