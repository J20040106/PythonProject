from random import randint
class Stack:
    data:list
    size:int
    def __init__(self) -> None:
        self.data=[]
        size=0
    def Push(self,num):#데이터 추가
        self.data.append(num)
        size+=1
        self.PrintData()
    def Pop(self):#데이터 삭제
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
    def Push(self,num):#데이터 추가
        self.data.append(num)
        size+=1
        self.PrintData()
    def Pop(self):#데이터 삭제
        if self.isEmpty()==False:
            del self.data[0]
        else:
            print("Queue is Empty")
    def isEmpty(self):
        return not self.data
    def PrintData(self):
        print(self.data)
class Sort:
    data=[]
    def PrintData(self):
        print(self.data)
    def __init__(self) -> None:
        self.Reset()
    def Reset(self):
        for i in  range(0,randint(5,10)):
            self.data.append(randint(0,100))
    def BubbleSort(self):#버블 정렬
        for i in range(0,len(self.data)-1):
            jmax=len(self.data)-1-i
            for j in range(0,jmax):
                if self.data[j]>self.data[j+1]:
                    tmp=self.data[j]
                    self.data[j]=self.data[j+1]
                    self.data[j+1]=tmp
    def SelectionSort(self):#선택 정렬
        for i in range(0,len(self.data)-1):
            for j in range(i,len(self.data)):
                if self.data[j]<self.data[i]:#data[i]를 최솟값으로 취급함
                    tmp=self.data[i]
                    self.data[i]=self.data[j]
                    self.data[j]=tmp