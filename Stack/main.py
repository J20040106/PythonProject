from stack import Stack
from random import randint

A=Stack()
for i in range(randint(0,100)):
    i=randint(0,1)
    if i==1:
        print("Push")
        A.Push(randint(0,100))
    else:
        print("PoP")    
        A.Pop()
    A.PrintData()