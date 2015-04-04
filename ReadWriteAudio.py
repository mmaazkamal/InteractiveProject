__author__ = 'HP'


import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from utility import pcm2float

sample_rate, x = wav.read('papa.wav')

xf= pcm2float(x, 'float32')
wav.write("temp1.wav", sample_rate,  xf )
wav.write("temp2.wav", sample_rate,  x )

print(len(xf)/float(sample_rate))


















# sample_rate1, x1 = wav.read('temp1.wav')
# #
# if (x==x1).all():
#     print(1)
# else:
#     print(2)
##################### Testing Cout #################

# plt.plot(xf)                                     #Plots
# plt.ylabel('some numbers')
# plt.show()

print(max(x[:,0]))
print(max(xf[:,0]))