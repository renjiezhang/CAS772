#import the pyplot and wavfile modules 
import matplotlib.pyplot as plot
from scipy.io import wavfile
from scipy import signal
import os
import soundfile as sf
import librosa
import librosa.display
import numpy as np
#import shutil

file_list=[]
typedir='157867'
for x in os.walk('Sound-Data/157867/'):
    file_list=x[2]
    
class_list=[]   
for f in file_list :
    fn='Sound-Data/157867/'+f
    #samplingFrequency, signalData = wavfile.read(fn)
    signalData, sample_rate = sf.read(fn)
    #melSample = librosa.feature.melspectrogram(signalData, sr=sample_rate, n_mels=128)
    frequencies, times, melSample = signal.spectrogram(signalData, sample_rate)
    #melSample=melSample.reshape(-1,1)
    signalData=signalData.reshape(-1)
    log_Sample = librosa.power_to_db(np.abs(librosa.stft(signalData))**2, ref=np.max)
    librosa.display.specshow(log_Sample)
    #librosa.display.specshow(log_Sample, sr=sample_rate, x_axis='time', y_axis='mel')  
#    signalData=signalData.reshape(-1)
#    print(f)
    #label = f.split('-')[0]

#    if label not in class_list:
#        os.mkdir('imgtut/home')
#        class_list.append(f)
    
    filename=str.replace(f,'.wav','.png')
    plot.savefig('imgtest/157867'+'/'+filename, bbox_inches='tight')
    plot.show()
    
#sub_dirs = [x[0] for x in os.walk('img/')]
#for sub_dir in sub_dirs:
#    if (len([name for name in os.listdir(sub_dir) if os.path.isfile(os.path.join(sub_dir, name))]))<2:
#        shutil.rmtree(sub_dir)






