import matplotlib.pyplot as plt
from scipy import stats

time = [0,1,2,3,4]
speed = [0,25,51,74,200]

slope, intercept, r, p, std_err = stats.linregress(speed,time)

def myfunc(speed):
  return slope * speed + intercept

model = list(map(myfunc,speed))

plt.scatter(speed,time)
plt.plot(speed,model)
print(r)
plt.show()


prediction = myfunc(30)
print(prediction)
