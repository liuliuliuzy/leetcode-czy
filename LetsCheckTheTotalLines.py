import os
import time

start = time.time()
totalLines = 0
totalFiles = 0
files = os.listdir('.')

for file in files:
    if file.startswith('.'):
        continue
    totalLines += len(open(file, 'r').readlines())
    totalFiles += 1
end = time.time()
print('Look Hooooow many lines of codes have you wrote\n===============================\nTotal Lines Count: {}\nTotal files Count: {}\nin {:.2}s\n==============================='.format(totalLines-13, totalFiles-3, end-start))