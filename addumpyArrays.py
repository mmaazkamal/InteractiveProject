__author__ = 'HP'

import numpy as np
# a = np.array([0, 10, 20, 30])
# b = np.array([20, 30, 40, 50, 60, 70])
# print(b)
# # c[:len(a)] += a
#
# b[1:len(a)+1]= b[1:(len(a)+1)]+2
#
#
# # Cout
#
# print(a)
# print(b)


##############  Audio Testing #############

import numpy
from pylab import *
import math

# # initialize all positions with 0
# arr = numpy.zeros(8)
# print arr
#
# # this modifies arr directly.
# # can be dangerous!
# def modify_array(arr):
#     # len(x) returns the length of x
#     for i in range(len(arr)):
#         arr[i] = math.exp(i)
#     return arr
#
# arr1 = numpy.zeros(8)
# arr1 = modify_array(arr1)
#
# arr2 = numpy.zeros(6)
# # do math on entire array at once
# arr2 = (arr2 + 1) * 400
#
# pylab.plot(arr1)
# pylab.plot(arr2)
# pylab.show()


import numpy
import scipy.io.wavfile
# the double ** is a power operator, i.e. 2^15
# convert_16_bit = float(2**15)
#
# sample_rate, samples = scipy.io.wavfile.read(
#     "a440-1second.wav")
# print "Data type is:", samples.dtype
#
# # scale to -1.0 -- 1.0
# samples = samples / (convert_16_bit + 1.0)
# print "Data type is now:", samples.dtype
#
# # change the file
# samples = samples * 0.25
#
# # scale to -32768 -- 32767
# samples = numpy.int16( samples * convert_16_bit )
# print "Data type is now:", samples.dtype
#
# scipy.io.wavfile.write("quieter.wav",
#     sample_rate, samples)




##################################################################################################3



#####################################################################################




from numpy.fft import fft, fftshift

# window = np.hanning(51)
# pylab.plot(window)
#
# pylab.title("Hann window")
#
# pylab.ylabel("Amplitude")
#
# pylab.xlabel("Sample")
#
# pylab.show()
#
# pylab.figure()
#
# A = fft(window, 2048) / 25.5
# mag = np.abs(fftshift(A))
# freq = np.linspace(-0.5, 0.5, len(A))
# response = 20 * np.log10(mag)
# response = np.clip(response, -100, 100)
# pylab.plot(freq, response)
#
# pylab.title("Frequency response of the Hann window")
#
# pylab.ylabel("Magnitude [dB]")
#
# pylab.xlabel("Normalized frequency [cycles per sample]")
#
# pylab.axis('tight')
#
# pylab.show()
##########################################

# # Number of samplepoints
# N = Fs
# # sample spacing
# T = 1.0 / 800.0
# #x = np.linspace(0.0, N*T, N)
#
# x=tBit
# #y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
#
# yf = fft(y)
# xf = np.linspace(0.0, 1.0/(2.0*T), N/2)
# import matplotlib.pyplot as plt
# plt.plot(xf, 2.0/N * np.abs(yf[0:N/2]))
# plt.grid()
# plt.show()






#######################################################

# Create Sinfile and write wav


## import file fomr matlab:

FsMat, yMat = scipy.io.wavfile.read(
    "papa(out)Mat1.wav")
print "Data type of yMAt is:", yMat.dtype

##


#
#
F, Fs,t, amp =20000, 44100,1, .5

convert_16_bit = float(2**15)
tBit=[ x/float(Fs) for x in range(0 ,t*Fs+1)]
tBit=tBit[1:len(tBit)]   # fix number of samples

y= numpy.zeros(len(tBit))

def modify_array(arr):
    # len(x) returns the length of x
    for i in range(len(arr)):
        y[i]= amp*math.sin(2*math.pi*F* arr[i])
       # print y[i]
    return arr
modify_array(tBit)
#win=np.hanning(len(y))
#y=y*win

print "Data type is now:", y.dtype
yPyt= numpy.int16( y*convert_16_bit )
print "Data type is now:", yPyt.dtype


scipy.io.wavfile.write("MatInPytOut.wav",FsMat, yMat)

# ##### prints  #####
# #
# figure(0)
# plot(yMat)
# #pylab.show()
#
# figure(1)
# plot(yPyt)
# show()

#
print len(yMat)
#print len(yPyt)
#
# print yMat[44100-1]
# print yPyt[44100-5]


#print len(tBit1)
# for yi in yMat:
#     print yi
# print "File Starts:"
# for yi in yPyt:
#     print yi





