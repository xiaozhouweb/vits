import os 
import soundfile  as sf
import librosa
import re 
# listFiles = os.listdir("./wavs")

# for fname in listFiles:
#   if re.match("(.*).wav.wav", fname, flags=0):
#     print(fname)
#     os.remove("./wavs/" +fname )
# print(len(listFiles))

# for i in listFiles:
#   try:
#     src_sig, sr = sf.read(f'./wavs/{i}' )  # name是要 输入的wav 返回 src_sig:音频数据  sr:原采样频率
#     dst_sig = librosa.resample(src_sig, sr, 22050)  # resample 入参三个 音频数据 原采样频率 和目标采样频率
#     sf.write(f'./wavs/{i}', dst_sig, 22050)  # 写出数据  参数三个 ：  目标地址  更改后的音频数据  目标采样数据
#   except Exception as e:
#     print(f'error =>{i}')

# print(listFiles)
# print(len(listFiles))
