#Define Class
class robot:
    #Define variables
    name = ''
    years = 0
    weight = 0
    __left_wheel = 0
    __right_wheel = 0

    def __init__(self,n,y,w,lw,rw):
        self.name = n
        self.years = y
        self.weight = w
        self.__left_wheel = lw
        self.__right_wheel = rw
    #Robot Actions
    def speak(self):
        print("My name is:%s" %self.name)
    def move_forward(self):
        self.__left_wheel = 1
        self.__right_wheel = 1
    def move_backward(self):
        self.__left_wheel = -1
        self.__right_wheel = -1
    def turn_left(self):
        self.__left_wheel = -1
        self.__right_wheel = 1
    def turn_right(self):
        self.__left_wheel = 1
        self.__right_wheel = -1
