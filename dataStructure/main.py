import DataStructure
from random import randint

A=DataStructure.Stack()
for i in range(randint(0,100)):
    i=randint(0,1)
    if i==1:
        A.Push(randint(0,100))
    else:    
        A.Pop()