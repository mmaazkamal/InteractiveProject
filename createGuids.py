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
convert_16_bit = float(2**15)


#end


guids=['{0:05b}'.format(x) for x in range(guidStart,2**nbits)] # Avialable Guids



sample_rate, x = wav.read('papa.wav')                   #Read input File
#x=.49*x                                                #Done later

amp,ampS,ampAudio, t= .49,.49,.49,.05                   #Variable handels for Bits
tBit = np.arange(0,t*sample_rate+1)/float(sample_rate)  #time Vector for Bits
F0,F1,Fsync = 19600, 19300, 19900                       #Bits Carrier Frequency


y0=amp*np.cos(2*np.pi*F0*tBit)                          #Bit0
winB=np.hanning(len(y0))                                #Applying Windows
y0=y0*winB

y1=amp*np.cos(2*np.pi*F1*tBit)                          #Bit1
y1=y1*winB                                              #Applying Windows

ysync=ampS*np.cos(2*np.pi*Fsync*tBit)                   #Bit for Synchronization
winS=np.hanning(len(ysync))                             #Applying Windows
ysync=ysync*winS

ySilence=amp*np.sin(2*np.pi*0*tBit)                     #Adding Silence in between all bits



y0=np.concatenate([ySilence,y0,ySilence,ysync])         #Bit0 coupled with silence and Sync
y1=np.concatenate([ySilence,y1,ySilence,ysync])         #Bit1 coupled with silence and Sync



fDelay=(nbits+1)+nbits+nbits*2                          #Complete Delay of the Signature
#  TODO: allow delay due to sound propagation



guids1=guids[0]                                         #First available guid
signature=ysync                                         #Declare and place Sync
for g in guids1:                                        #Complete Concatenated Signature
    if g=='0':                                          # concatenate Bit0
        signature=np.concatenate([signature,y0])
    else:                                               # concatenate Bit1
        signature=np.concatenate([signature,y1])



print "1 Data type is:", x.dtype                        # Confirm Audio Tyspe before conversion; this should int16
xNormalized = (x / (convert_16_bit + 1.0))*ampAudio          # Normalize and convert to float64 and recale it to max amplitude at .49
print "2 Data type is:", xNormalized.dtype              # Confirm Audio Type after  conversion; this should float64



indexEmbed=timeEmbed*sample_rate - fDelay               #Interactive Index after accounting for the delays



xNormalized[indexEmbed:indexEmbed+len(signature),1]= xNormalized[indexEmbed:indexEmbed+(len(signature)),1]+signature # embed signature in channel1
xNormalized[indexEmbed:indexEmbed+len(signature),0]= xNormalized[indexEmbed:indexEmbed+(len(signature)),0]+signature # embed signature in channel0



xNormalized= np.int16( xNormalized * convert_16_bit )    # convert Audio data to 1nt16
print "3 Data type is:", xNormalized.dtype               # Confirm Audio Type ; this should int16 for wavwriting



wav.write("papa(out)Pyt.wav",sample_rate,xNormalized )    #export interactive audio

##################### Testing Cout #################

plt.plot(xNormalized[:,1])                                     #Plots
plt.ylabel('some numbers')
plt.show()


# print(type(xNormalized))

# print(len(signature))
# print(len(xNormalized[indexEmbed:len(signature)+indexEmbed,1]))
#print(fDelay*len(tBit))

# print(xNormalized[1:10,1])

#
# print(max(xNormalized[:,0]))
# print(max(xNormalized[:,1]))