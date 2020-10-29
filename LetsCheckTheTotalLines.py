import os
import time

start = time.time()
totalLines = 0
files = os.listdir('.')

for file in files:
    if file.startswith('.'):
        continue
    totalLines += len(open(file, 'r').readlines())
end = time.time()
print('Look Hooooow many lines of codes have you wrote\n===============================\nTotal Lines Count: {} in {:.2}s\n==============================='.format(totalLines-13, end-start))