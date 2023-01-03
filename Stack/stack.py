class Stack:
    data:list
    def __init__(self) -> None:
        self.data=[]
    def Push(self,num):
        self.data.append(num)
    def Pop(self):
        if self.isEmpty()==False:
            self.data.pop()
        else:
            print("stack is Empty")
    def isEmpty(self):
        return not self.data
    def PrintData(self):
        print(self.data)