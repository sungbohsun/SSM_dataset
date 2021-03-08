import os
import torch
import librosa
import warnings
warnings.filterwarnings("ignore")

from glob import glob
from tqdm import tqdm
from shutil import copyfile
from multiprocessing import Process, Pool

def save(k):
    print('start process')
    data = {}
    for c in tqdm(range(k,k+100)):
        if c != k and (c+1) % 100 == 0:
            torch.save(data,'x/dic_{}.pt'.format(str(c+1)))
            data = {}
        try:
            x ,sr = librosa.load('audio_rename/{}.mp3'.format(IDs[c]),sr=16000)
            data[IDs[c]] = x
        except:
            continue

if __name__ == '__main__':  

    if not os.path.isdir('x'):
        os.mkdir('x')

#     names = sorted(glob('audio_dl/*/*mp3'))
#     for name in tqdm(names):
#         src = name
#         dst = 'audio_rename/'+name[-15:]
#         copyfile(src, dst)

    IDs = [n.split('/')[1].split('.')[0] for n in sorted(glob('audio_rename/*mp3'))]
    input_ = list(range(0,len(IDs),100))
    
    pool = Pool(len(input_))

      # 運行多處理程序
    pool_outputs = pool.map(save, input_)
