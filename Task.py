from playsound import playsound 
import os
import json
audioFiles = []
OutputFile = {}
OutputFile['InformatioanAboutAudioFiles'] = []
Audiodirectoy = input("Please input the directory of audio files: ")
os.chdir(Audiodirectoy)
allfiles = os.listdir(os.getcwd()) 
print(allfiles)
for item in allfiles: 
    if item.endswith('.mp3') or item.endswith('.wav') or item.endswith('.wma'):
        audioFiles.append(item)
if len(audioFiles) == 0 :
    print(Audiodirectoy + " Doesn't contain any audio file")
    quit()


for i in audioFiles:
    print("Now is playing " + i + " audio")   
    playsound(i)
    UsrInp = input('Please press c if ' + i + ' sound is Clean, otherwise press n for Noisy. Please note that program is cansesensitive, dont use uppercases ')
    if UsrInp == 'c': 
        OutputFile['InformatioanAboutAudioFiles'].append({
        i : "Clean"
        })

    elif UsrInp == 'n': 
        OutputFile['InformatioanAboutAudioFiles'].append({
        i : "Noisy"
        })
    else :
        OutputFile['InformatioanAboutAudioFiles'].append({
        i : "Unknown"
        })



with open('audio_labels.json', 'w') as outfile:
    json.dump(OutputFile, outfile)