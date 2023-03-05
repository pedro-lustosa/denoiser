import os
from pydub import AudioSegment
import shutil

WRITE_INPUT_DIRECTORY='./dataset/debug/noisy/'
WRITE_OUTPUT_DIRECTORY='./dataset/debug/clean_posprocessed/'
READ_INSTRUMENTAL_DIRECTORY='./dataset/debug/instrumental/'
READ_VOICE_DIRECTORY='./dataset/debug/clean/'

instrumental_files=os.listdir(READ_INSTRUMENTAL_DIRECTORY)
instrumental_files.sort()
voice_files=os.listdir(READ_VOICE_DIRECTORY)
voice_files.sort()
voice_files = voice_files[:-6]

for i in instrumental_files:
    instrumentalAudio = AudioSegment.from_wav(READ_INSTRUMENTAL_DIRECTORY + i)
    for v in voice_files:
        voiceAudio = AudioSegment.from_wav(READ_VOICE_DIRECTORY+v)
        cut = min(len(instrumentalAudio),len(voiceAudio))
        instrumentalAudio_cutted = instrumentalAudio[:cut]
        voiceAudio = voiceAudio[:cut]
        voiceAudio = voiceAudio + 9
        inputAudio = instrumentalAudio_cutted.overlay(voiceAudio)
        inputAudio = inputAudio.set_frame_rate(24000)
        inputAudio = inputAudio.split_to_mono()
        outputAudio = voiceAudio.set_frame_rate(24000)
        outputAudio = outputAudio.split_to_mono()
        outputAudio[0].export(WRITE_OUTPUT_DIRECTORY + v[:-4] + i[:-4] + 'LEFT.wav', format="wav")
        inputAudio[0].export(WRITE_INPUT_DIRECTORY + v[:-4] + i[:-4]+'LEFT.wav', format="wav")
        try:
            outputAudio[1].export(WRITE_OUTPUT_DIRECTORY + v[:-4] + i[:-4] + 'RIGHT.wav', format="wav")
            inputAudio[1].export(WRITE_INPUT_DIRECTORY + v[:-4] + i[:-4] + 'RIGHT.wav', format="wav")
        total, used, free = shutil.disk_usage("/")
        free = free // (2**30)
        if free <= 50:
            break
        except:
            pass

files=os.listdir(WRITE_INPUT_DIRECTORY)
files.sort()
time=0

for i in files:
    audio = AudioSegment.from_wav(WRITE_INPUT_DIRECTORY + i)
    time = time + audio.frame_count()/(24000*60)

print(time/60)
