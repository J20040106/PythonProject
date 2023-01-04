class Stack:
    data:list
    size:int
    def __init__(self) -> None:
        self.data=[]
        size=0
    def Push(self,num):
        self.data.append(num)
        size+=1
        self.PrintData()
    def Pop(self):
        if self.isEmpty()==False:
            self.data.pop()
            size-=1
            self.PrintData()
        else:
            print("stack is Empty")
    def isEmpty(self):
        return not self.data
    def PrintData(self):
        print(self.data)
class Queue:
    data:list
    size:int
    def __init__(self) -> None:
        self.data=[]
        size=0
    def Push(self,num):
        self.data.append(num)
        size+=1
        self.PrintData()
    def Pop(self):
        if self.isEmpty()==False:
            del self.data[0]
        else:
            print("Queue is Empty")
    def isEmpty(self):
        return not self.data
    def PrintData(self):
        print(self.data)