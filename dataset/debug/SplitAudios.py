import os
from pydub import AudioSegment

WRITE_INPUT_DIRECTORY='./debug/noisy/'
WRITE_OUTPUT_DIRECTORY='./debug/clean_posprocessed/'
READ_INPUT_DIRECTORY='./debug/noisy/'
READ_OUTPUT_DIRECTORY='./debug/clean_posprocessed/'
SplitNumber=3

input_files=os.listdir(READ_INPUT_DIRECTORY)
input_files.sort()
#input_files=input_files[:-6]
output_files=os.listdir(READ_OUTPUT_DIRECTORY)
output_files.sort()
#output_files=output_files[:-6]

for i in input_files:
    audio = AudioSegment.from_wav(READ_INPUT_DIRECTORY+i)
    duration = audio.duration_seconds*1000
    for n in range(0,SplitNumber):
        splitted=audio[n*duration/SplitNumber:(n+1)*duration/SplitNumber]
        splitted.export(WRITE_INPUT_DIRECTORY+i[:-4]+'splitted_'+str(n)+'.wav', format="wav")

for o in output_files:
    audio = AudioSegment.from_wav(READ_OUTPUT_DIRECTORY+o)
    duration = audio.duration_seconds*1000
    for n in range(0,SplitNumber):
        splitted=audio[n*duration/SplitNumber:(n+1)*duration/SplitNumber]
        splitted.export(WRITE_OUTPUT_DIRECTORY+o[:-4]+'splitted_'+str(n)+'.wav', format="wav")