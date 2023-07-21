'''
Подсчет частот слов, начинающихся буквой a
'''
import time
#import gzip
#import shutil

freqs = {}

# with gzip.open('googlebooks-eng-all-1gram-20120701-a.gz', 'rb') as f_in:
#    with open('googlebooks-eng-all-1gram-20120701-a.txt', 'wb') as f_out:
#        shutil.copyfileobj(f_in, f_out)

with open('googlebooks-eng-all-1gram-20120701-a.txt', encoding='utf-8') as f:
    lines = f.readlines()

    start = time.time()

    for line in lines:
        data = line.split('\t')
        word = data[0]
        count = int(data[2])
        if word in freqs:
            freqs[word] = freqs[word] + count
        else:
            freqs[word] = count

    end = time.time()
    print(f'{end - start:.4f}')
