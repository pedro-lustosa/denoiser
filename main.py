import torch
import torchaudio
from denoiser import pretrained
from denoiser.dsp import convert_audio
import wave
import struct

model = pretrained.dns64().cuda()
wav1, sr = torchaudio.load('teste.wav')
T1=wav1
T2=wav1
T1[1]=wav1[0]
T2[0]=wav1[1]
wav2T1 = convert_audio(T1.cuda(), sr, model.sample_rate, model.chin)
wav2T2 = convert_audio(T2.cuda(), sr, model.sample_rate, model.chin)
with torch.no_grad():
    denoisedL = model(wav2T1[None])[0]
    denoisedR = model(wav2T2[None])[0]


wav3L=wav2T1.data.cpu().numpy()
wav3R=wav2T2.data.cpu().numpy()
denoisedL=denoisedL.data.cpu().numpy()
denoisedR=denoisedR.data.cpu().numpy()

samples = wav3L.size
#fr = model.sample_rate
fr = 44100
comptype = "NONE"
compname = "not compressed"
nchannels = 2
sampwidth = 2
amp = 50000

wav_file = wave.open("original.wav", "w")

wav_file.setparams((nchannels, sampwidth, fr, samples, comptype, compname))
wav4L=list(wav3L[0])
wav4R=list(wav3R[0])

for s, t in zip(wav4L, wav4R):
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.writeframes(struct.pack('h', int(t*amp/2)))

wav_file.close()

wav_file = wave.open("denoised.wav", "w")
wav_file.setparams((nchannels, sampwidth, fr, samples, comptype, compname))
denoisedL=list(denoisedL[0])
denoisedR=list(denoisedR[0])

for s, t in zip(denoisedL, denoisedR):
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.writeframes(struct.pack('h', int(t*amp/2)))

wav_file.close()