import math
import wave
import struct
import numpy

freq = 440.0
data_size = 40000
fname = "WaveTest.wav"
frate = 11025.0  # framerate as a float
amp = 64000.0     # multiplier for amplitude

sine_list_x = []
sine_list_y = []
for x in range(data_size):
    sine_list_x.append(math.sin(2*math.pi*freq*(x/frate)))
    sine_list_y.append(math.sin(2 * math.pi * 0.73*freq * (x / frate)))

wav_file = wave.open(fname, "w")

nchannels = 2
sampwidth = 2
framerate = int(frate)
nframes = data_size
comptype = "NONE"
compname = "not compressed"

#wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))

'''
for s, t in zip(sine_list_x, sine_list_y):
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))
    wav_file.writeframes(struct.pack('h', int(t * amp / 2)))
'''

#wav_file.close()

teste=wave.open('iwannabeyours_female_2_21.0.wav','rb')
samples = teste.getnframes()
audio = teste.readframes(samples)

audio_as_np_int16 = numpy.frombuffer(audio, dtype=numpy.int16)
audio_as_np_float64 = audio_as_np_int16.astype(numpy.float64)

max_int16 = 2**15
audio_normalised = audio_as_np_float64 / max_int16
a=list(audio_normalised)

wav_file.setparams((nchannels, sampwidth, teste.getframerate(), samples, comptype, compname))

for s in a:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s*amp/2)))

wav_file.close()