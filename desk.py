
import numpy as np
import scipy
import show

DIRPATH = "./sample/" # wav 파일이 있는 위치
filename = "canon_mono.wav" # wav 파일 이름
#filename = "001_G.wav"


# wav 파일을 받아서 샘플링 레이트, 변위 데이터 구하기
# data 는 (1 / sample_rate)초 단위로 구한 변위
sample_rate, data = scipy.io.wavfile.read(DIRPATH + filename)



#show.show_freq(filename, data, sample_rate)
#show.show_amp(filename, data, sample_rate)

rate = sample_rate // 60
lst = []

for i in range(len(data) // rate):
    lst.append(np.abs(data[i * rate : (i + 1) * rate]).mean())

print("rate:", rate)
show.show_amp(filename, data, sample_rate)
show.show_amp(filename, np.abs(data), sample_rate)
show.show_amp(filename, lst, rate)