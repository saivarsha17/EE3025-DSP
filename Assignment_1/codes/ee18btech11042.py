import soundfile as sf
from scipy import signal

import numpy as np
import matplotlib.pyplot as plt
#if using termux
#import subprocess
#import shlex
#end if
input_signal,fs = sf.read('Sound_Noise.wav')

samplfreq=fs

order=4

cutoff_freq=4000.0

Wn=2*(cutoff_freq/samplfreq)
b,a = signal.butter(order,Wn,'low')

W = np.arange(len(input_signal))/len(input_signal)
z = np.exp(-1j*2*(np.pi)*W)
H = np.polyval(b,z)/np.polyval(a,z)
input_signal_fft = np.fft.fft(input_signal)
Y = H*input_signal_fft
y = np.fft.ifft(Y).real

t = []
for  i in range(0,len(input_signal)):
  t.append(i/samplfreq)
f1 = plt.figure(figsize=(10,11))

plt.subplot(2,1,1)
plt.plot(t,y)
plt.title(" With your own routine")
plt.xlabel("t")
plt.ylabel("y(n)")
plt.grid()




output_signal = signal.filtfilt(b, a,input_signal)

plt.subplot(2,1,2)
plt.plot(t,output_signal)
plt.title("With routine")
plt.xlabel("t")
plt.ylabel("y(n)")
plt.grid()
plt.savefig('../figs/ee18btech11042_1.eps')
plt.savefig('../figs/ee18btech11042_1.pdf')
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11042_1.pdf"))  #if using termex
output_signal_fft = np.fft.fft(output_signal)

freq_fft = []
for i in range(0,len(input_signal)):
  freq_fft.append(-np.pi + i*2*np.pi/len(input_signal))
f2 = plt.figure(figsize=(10,11))
plt.subplot(2,1,1)
plt.plot(freq_fft,abs(np.fft.fftshift(Y)))
plt.title(" With your own routine")
plt.xlabel("w")
plt.ylabel("|Y(jw)|")
plt.grid()
plt.subplot(2,1,2)

plt.plot(freq_fft,abs(np.fft.fftshift(output_signal_fft)))
plt.title(" With routine" )
plt.xlabel("w")
plt.ylabel("|Y(jw)|")
plt.grid()
plt.savefig('../figs/ee18btech11042_2.pdf')
plt.savefig('../figs/ee18btech11042_2.eps')
#subprocess.run(shlex.split("termux-open ../figs/ee18btech11042_2.pdf"))  #if using termex
sf.write('Soundwith_reducedNoise_routine.wav',output_signal,fs)
sf.write('Soundwith_reducedNoise_with your routine.wav',y,fs)



plt.show()
