
import numpy as np
import matplotlib.pyplot as plt
import struct
from scipy.fftpack import fft
from scipy.io import wavfile

wav_path = "./sample"
file_name = "test(440, 30000).wav"
file_name = "canon_mono.wav"
with open(wav_path + "/" + file_name, "br") as fin:
    a = fin.read()

period = None
frequency = None

def header_checker(data):
    if(len(data) != 44):
        print("give me just header")
    if(data[:4] != b"RIFF"):
        print("Error")
    print(data[:4])
    print("chunk size:", struct.unpack("<L", data[4:8]))
    if(data[8:12] != b"WAVE"):
        print("Error")
    print(data[8:12])
    if(data[12:16] != b"fmt "):
        print("Error")
    print(data[12:16])
    if(struct.unpack("<L", data[16:20])[0] != 16):
        print("Error")
    print("subchunk:", struct.unpack("<L", data[16:20]))
    print("audio format:", struct.unpack("<H", data[20:22]))
    print("numChannels:", struct.unpack("<H", data[22:24]))
    print("sampleRate:", struct.unpack("<L", data[24:28]))
    print("ByteRate:", struct.unpack("<L", data[28:32]))
    print("BlockAligh:", struct.unpack("<H", data[32:34]))
    print("BitPerSample:", struct.unpack("<H", data[34:36]))
    if(data[36:40] != b"data"):
        print("Error")
    print("SubChunk2 Size:", struct.unpack("<L", data[40:44]))
    global period
    period = struct.unpack("<L", data[40:44])[0] / struct.unpack("<L", data[28:32])[0]
    global frequency
    frequency = struct.unpack("<L", data[24:28])[0]
    
print(len(a))

header_checker(a[:44])

fs, data = wavfile.read(wav_path + "/" + file_name) # load the data


print(period)









