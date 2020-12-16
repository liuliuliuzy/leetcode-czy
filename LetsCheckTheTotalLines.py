import os
import time
from collections import defaultdict

start = time.time()
totalLines = 0
totalFiles = 0
files = os.listdir('.')
filesTypes = defaultdict(int)

colors = ["\033[{}m".format(i) for i in range(31, 38)]
endColor = "\033[0m"

for file in files:
    if file.startswith('.'):
        continue
    totalFiles += 1
    totalLines += len(open(file, 'r', encoding='UTF-8').readlines())
    filesTypes[os.path.splitext(file)[1]] += 1
    
end = time.time()
print(
'''Look Hooooow many lines of codes have you written :)
==============================================================
Total Lines Count: \033[36m{}\033[0m
Total files Count: \033[35m{}\033[0m
in {:.3}s
As for the file types:'''.format(totalLines-13, totalFiles-3, end-start))

startColorIndex = 0
for key, value in filesTypes.items():
    if startColorIndex > len(colors)-1: startColorIndex = 0
    print(colors[startColorIndex] + "{:6}: ".format(key) + "+"*max(int((value/totalFiles)//0.01), 1)+ " {:.2%}".format(value/totalFiles) + endColor)
    startColorIndex += 1

print("==============================================================")