from car import Car
import random
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as fm


fm.get_fontconfig_fonts()

font_location = 'C:/Windows/Fonts/H2HDRM.TTF'
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)


x=[[],[]]
y=[[],[]]
for i in range(1,random.randint(10,20)):
    Tmp=Car()
    x[0].append(str(i)+"번 차")
    y[0].append(Tmp.speed)

carData=Car()
x[1].append("처음")
y[1].append(carData.speed)
for i in range(1,random.randint(5,10)):
    r=random.randint(0,1)
    if r==0:
        carData.Up()
    else:
        carData.Down()
    x[1].append(str(i)+"시간 후")
    y[1].append(carData.speed)

plt.subplot(2,1,1)

# x[0]과 y[0]을 이용해 막대 그래프 생성
result=plt.bar(x[0], y[0])
plt.xticks(x[0],x[0])
# 그래프 제목 추가
plt.title('각 차의 최고 속도')
for rect in result:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%dkm/h' % height, ha='center', va='bottom', size = 8)

plt.subplot(2,1,2)
# x[0]과 y[0]을 이용해 막대 그래프 생성
plt.plot(x[1],y[1])
for i in range(len(x[1])):
    height = y[1][i]
    plt.text(x[1][i], height + 0.25, '%d km/h' %height, ha='center', va='bottom', size = 8)
# 그래프 제목 추가
plt.title('시간당 속도 변화율')
# 그래프 출력
plt.show()
