% __author__ = 'HP'
clc 
clear all
%%variable handels
guidStart=8;
nbits=5;
timeEmbed=7;


%%guids Read

guidsInt=[guidStart:2^nbits-1];
guids= fliplr(de2bi(guidsInt,5));
    
%%Read Audio

[x, sample_rate] = wavread('papa.wav');                   %Read input File
x=.49*x;
[Fs, amp,ampS, t]= deal(sample_rate, .49, .49, .05) ;       %Variable handels for Bits
%tBit = np.arange(0,t*Fs+1)/float(Fs)                 %time Vector for Bits
tBit=[0:t*Fs]/Fs;

[F0,F1,Fsync] = deal(19600, 19300, 19900)   ;                    %Bits Carrier Frequency

y0=amp*cos(2*pi*F0*tBit);                       %Bits
L=length(y0);
w=hann(L);
y0=times(y0,w');

y1=amp*cos(2*pi*F1*tBit);

 L=length(y1);
w=hann(L);
y1=times(y1,w');

ySilence=amp*sin(2*pi*0*tBit);

ysync=ampS*cos(2*pi*Fsync*tBit);
 Ls=length(ysync);
ws=hann(Ls);
ysync=times(ysync,ws');

%plot(y0)
y0=horzcat(ySilence,y0,ySilence,ysync);         %Bits coupled with silence and Sync
y1=horzcat(ySilence,y1,ySilence,ysync); 
%figure
%disp('length of y0='); length(y0)
%plot(y0)

 
fDelay=(nbits+1)+nbits+nbits*2;                          %Complete Delay of the Signature
guids1=guids(1,:);                                        %First available guid

signature=ysync;                                         %Declare and place Sync
for i=1:length(guids1)                      %Complete Signature
    if guids1(i)==0
        signature=horzcat(signature,y0);
        guids1(i);
    else
        signature=horzcat(signature,y1);
        guids1(i);
    end
end

signature=signature';
%plot(signature)


xNormalized = x;
indexEmbed=timeEmbed*sample_rate - fDelay*L    ;          %interactive Index
disp('start time embedding in 1 :')
indexEmbed/sample_rate
%indexEmbed=191961
%% embedding 1

xNormalized(indexEmbed:indexEmbed+length(signature)-1,1)= xNormalized(indexEmbed:indexEmbed+(length(signature)-1),1)+signature; % embed signature
%xNormalized(indexEmbed:indexEmbed+length(signature)-1,2)= xNormalized(indexEmbed:indexEmbed+(length(signature)-1),2)+signature; % embed signature
indexEmbed1End=indexEmbed+length(signature)-1;
wavwrite(xNormalized,sample_rate, 'papa(out)Mat1.wav');

%% embedding 2

x2=separateEmbedding(x);
wavwrite(x2,sample_rate, 'papa(out)Mat2.wav');

