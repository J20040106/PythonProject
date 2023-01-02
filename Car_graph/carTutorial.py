from car import Car
import random
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm
from graph import Graph


fm.get_fontconfig_fonts()

font_location = 'C:/Windows/Fonts/H2HDRM.TTF'
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)


data=[Graph(),Graph()]
for i in range(1,random.randint(10,20)):
    Tmp=Car()
    data[0].x.append("차"+str(i))
    data[0].y.append(Tmp.speed)

carData=Car()
data[1].x.append("처음")
data[1].y.append(carData.speed)
for i in range(1,random.randint(5,10)):
    r=random.randint(0,1)
    if r==0:
        carData.Up()
    else:
        carData.Down()
    data[1].x.append(str(i)+"시간 후")
    data[1].y.append(carData.speed)

plt.subplot(2,1,1)

# x[0]과 y[0]을 이용해 막대 그래프 생성
result=plt.bar(data[0].x, data[0].y)
plt.xticks(data[0].x,data[0].x)
# 그래프 제목 추가
plt.title('각 차의 속도')
for rect in result:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', size = 8)

plt.subplot(2,1,2)
# x[0]과 y[0]을 이용해 막대 그래프 생성
plt.plot(data[1].x,data[1].y)
for i in range(len(data[1].x)):
    height = data[1].y[i]
    plt.text(data[1].x[i], height + 0.25, '%.1f' %height, ha='center', va='bottom', size = 8)
# 그래프 제목 추가
plt.title('시간당 속도 변화율')

# 그래프 출력
plt.show()
