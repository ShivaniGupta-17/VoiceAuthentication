import pickle
from read_audio import read_file
from models import generate_codebook
from collections import defaultdict
import pyaudio
import wave

def microphone_integration(file_name):
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 48000
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = file_name+ ".wav"
     
    audio = pyaudio.PyAudio()
     
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print ("recording...")
    frames = []
     
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording")
 
 
    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
     
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

def write_file_for_microphone():
    Input1=input("Enter speaker name")
    microphone_integration(Input1)
    Ip=Input1+".wav"
    Input2=read_file(Ip)
    codes, codebook_abs_weights, codebook_rel_weights = generate_codebook(Input2, size_codebook=10, epsilon=0.00001)
    dictionary=defaultdict()
    
    try:
        with open("Voicerecognition.pkl","rb") as pkl:
            print("tryZEROTHITERATION")
            G=pickle.load(pkl)
            print("TRYYYYYYYYYYYYY")
            print(G,"\n\n\n")
            print(type(G))
            G[Input1]=codes
            print("FINAL TRYYYYYYYYYYYYYYY")
            return G
    except:
        with open("Voicerecognition.pkl","wb") as pkl:
            dictionary={}
            print("EXCEPTTTTTTT")
            dictionary[Input1]=codes
            return dictionary
#            pickle.dump(dictionary,pkl)
    
def file_call_microphone():
    try:
        G1=write_file_for_microphone()
        with open("Voicerecognition.pkl","wb") as pkl3:
            pickle.dump(G1,pkl3)
        print("DONEEEE")
    except:
        print("EXCEPTT")
        write_file_for_microphone()

def process_new_input_microphone():
    Ip1=input("Enter speaker name")
    microphone_integration(Ip1)
    Ip0=Ip1+".wav"
    Ip2=read_file(Ip0)
    
    return Ip1,Ip2
