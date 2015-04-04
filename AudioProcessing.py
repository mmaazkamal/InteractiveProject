__author__ = 'HP'

__author__ = 'HP'
import numpy as np
import matplotlib.pyplot as plt
from utility import pcm2float
from utility import float2pcm
import scipy.io.wavfile as wav



#variable handels
guidStart=8
nbits=5
timeEmbed=5

#end

guids=['{0:05b}'.format(x) for x in range(guidStart,2**nbits)] # Avialable Guids


sample_rate, x = wav.read('papa.wav')                   #Read input File
Fs, amp,ampS, t= sample_rate, .2, .6, .05,        #Variable handels for Bits
tBit = np.arange(0,t*Fs+1)/float(Fs)                 #time Vector for Bits
F0,F1,Fsync = 19600, 19300, 19900                       #Bits Carrier Frequency

y0=amp*np.cos(2*np.pi*F0*tBit)                          #Bits
y1=amp*np.cos(2*np.pi*F1*tBit)
ySilence=amp*np.sin(2*np.pi*0*tBit)
ysync=ampS*np.cos(2*np.pi*Fsync*tBit)

y0=np.concatenate([ySilence,y0,ySilence,ysync])         #Bits coupled with silence and Sync
y1=np.concatenate([ySilence,y1,ySilence,ysync])

fDelay=(nbits+1)+nbits+nbits*2                          #Complete Delay of the Signature
guids1=guids[0]                                         #First available guid
print(guids1)
signature=ysync                                         #Declare and place Sync
for g in guids1:                       #Complete Signature
    if g=='0':
        signature=np.concatenate([signature,y0])
        #print(g)
    else:
        signature=np.concatenate([signature,y1])
        #print(g)

print "1 Data type is:", x.dtype
convert_16_bit = float(2**15)
xNormalized = x / (convert_16_bit + 1.0)
print "2 Data type is:", xNormalized.dtype


# print(max(xNormalized[:,0]))
# print(max(xNormalized[:,1]))

indexEmbed=timeEmbed*sample_rate - fDelay               #interactive Index
xNormalized[indexEmbed:indexEmbed+len(signature),1]= xNormalized[indexEmbed:indexEmbed+(len(signature)),1]+signature # embed signature
xNormalized[indexEmbed:indexEmbed+len(signature),0]= xNormalized[indexEmbed:indexEmbed+(len(signature)),0]+signature # embed signature


xNormalized= np.int16( xNormalized * convert_16_bit )
print "3 Data type is:", xNormalized.dtype
###############################

wav.write("papa2.wav", sample_rate,  xNormalized )  #export interactive audio

##################### Testing Cout #################

# plt.plot(xNormalized)                                     #Plots
# plt.ylabel('some numbers')
# plt.show()


# print(type(xNormalized))

# print(len(signature))
# print(len(xNormalized[indexEmbed:len(signature)+indexEmbed,1]))
#print(fDelay*len(tBit))

# print(xNormalized[1:10,1])


print(max(xNormalized[:,0]))
print(max(xNormalized[:,1]))