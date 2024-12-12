import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

time = [5,7,8,2,9]
speed = [10,53,21,79,34]

mymodel = np.poly1d(np.polyfit(speed, time, 3))

myline = np.linspace(0, 79, 100)

plt.scatter(speed,time)
plt.plot(myline, mymodel(myline))
print(r2_score(time, mymodel(speed)))
plt.show()

speed = mymodel(40)
print(speed)