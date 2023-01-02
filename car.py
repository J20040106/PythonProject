import random
class Car:
    speed:int
    def __init__(self):
        self.speed=random.randint(10,100)
    def Up(self):
        self.speed+=random.randint(10,50)
    def Down(self):
        self.speed-=random.randint(10,50)
        if self.speed<0:
            self.speed=0
    def Result(self):
        print(self.speed)
