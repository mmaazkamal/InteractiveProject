__author__ = 'HP'
import numpy as np
import matplotlib.pyplot as plt

Fs=44100
pc=3
tc = np.arange(0,pc*Fs+1)/float(Fs)

print(tc)
i=tc[len(tc)-44100]
print(i)

amp=.5
Fs = 5
ys=amp*np.cos(2*np.pi*Fs*tc)

print(amp*np.cos(2*np.pi*Fs*i))

plt.plot(ys)
plt.ylabel('some numbers')
plt.show()