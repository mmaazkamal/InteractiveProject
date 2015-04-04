F1=20000;
Fs= 44100;
p=1;
amp=.5;
%convert_16_bit = float(2**15);

tc =[0:1:p*Fs]/Fs;
tc=tc(2:length(tc));

%print tBit[5]*float(math.pi)
l= length(tc)/Fs

y=amp*cos(2*pi*F1*tc);
%Ls1=length(ys);
%ws1=hann(Ls1);
%ys=times(ys,ws1');

wavwrite(y,Fs, 'audio1Matlab.wav');