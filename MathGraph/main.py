from sympy import symbols, Derivative
import matplotlib.pyplot as plt
from random import randint

def Function(x):
    return x**2
    
data=symbols('x')
f=data**2
fprime=Derivative(f,data).doit()
x=[]
y=[[],[]]
m=randint(50,100)
for i in range(-m,m):
    x.append(i)
    y[0].append(Function(i))
    y[1].append(fprime.subs({data:i}))
plt.plot(x,y[0],x,y[1])
plt.show()
print(fprime)