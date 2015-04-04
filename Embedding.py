__author__ = 'HP'


from scipy.io import wavfile
#from utility import pcm2float
import numpy as np
import matplotlib.pyplot as plt


fs, sig = wavfile.read('papa.wav')
print(len(sig))
def pcm2float(sig, dtype=np.float64):
    sig = np.asarray(sig)  # make sure it's a NumPy array
    assert sig.dtype.kind == 'i', "'sig' must be an array of signed integers!"
    dtype = np.dtype(dtype)  # allow string input (e.g. 'f')

    # Note that 'min' has a greater (by 1) absolute value than 'max'!
    # Therefore, we use 'min' here to avoid clipping.
    return sig.astype(dtype) / dtype.type(-np.iinfo(sig.dtype).min)


normalized = pcm2float(sig, 'float32')


Fs=44100
pc=3
#tc = [0:pc*Fs+1]/Fs
tc=[]
for i in range(0,pc*Fs+1):
    tc.append(i/Fs)


amp=.5
Fs = 19900
ys=amp*np.cos(2*np.pi*Fs*tc)





print(len(normalized))

FOURIE=np.fft.rfft(normalized)
#plt.plot(abs(FOURIE))
plt.plot(ys)
plt.ylabel('some numbers')
plt.show()

