import os
import time
from collections import defaultdict

start = time.time()
totalLines = 0
totalFiles = 0
files = os.listdir('.')
filesTypes = defaultdict(int)


for file in files:
    totalFiles += 1
    if file.startswith('.'):
        continue
    totalLines += len(open(file, 'r', encoding='UTF-8').readlines())
    filesTypes[os.path.splitext(file)[1]] += 1
    
end = time.time()
print(
'''Look Hooooow many lines of codes have you wrote
===============================
Total Lines Count: {}
Total files Count: {}
in {:.2}s
==============================='''
    .format(totalLines-13, totalFiles-3, end-start))