F1=20000;
Fs= 48000;
p=1;
amp=.5;
%convert_16_bit = float(2**15);

tc = [0:p*Fs+1]/Fs;
%print tBit[5]*float(math.pi)

ys=amp*cos(2*pi*F1*tc);
Ls1=length(ys);
ws1=hann(Ls1);
ys=times(ys,ws1');


y=ys;
L=length(ys);
Fs=Fs
NFFT = 2^nextpow2(L); % Next power of 2 from length of y
Y = fft(y,NFFT)/L;
f = Fs/2*linspace(0,1,NFFT/2+1);

% Plot single-sided amplitude spectrum.
plot(f,2*abs(Y(1:NFFT/2+1))) 
title('Single-Sided Amplitude Spectrum of y(t)')
xlabel('Frequency (Hz)')
ylabel('|Y(f)|')


%%%%%%%%%%%%%%%%%%%
figure


y=data;
L=length(y);
Fs=fs
NFFT = 2^nextpow2(L); % Next power of 2 from length of y
Y = fft(y,NFFT)/L;
f = Fs/2*linspace(0,1,NFFT/2+1);

% Plot single-sided amplitude spectrum.
plot(f,2*abs(Y(1:NFFT/2+1))) 
title('Single-Sided Amplitude Spectrum of y(t)')
xlabel('Frequency (Hz)')
ylabel('|Y(f)|')


