import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sigtool


data = np.genfromtxt(
    r"signal.csv", delimiter=',')

plt.plot(data, color='b', label='signal')

env = np.abs(sigtool.hilbert(data))
treshold = np.max(env)/2
square_sig = (env > treshold) #* np.max(env)

plt.plot(env, color='r', label='env')
plt.plot(square_sig, color='g', label='square')
print(square_sig.where(1)[0])

plt.legend()
plt.show()
