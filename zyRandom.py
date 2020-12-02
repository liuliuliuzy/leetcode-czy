from random import randrange
import time
import random
from typing import List

def createRandList(low: int, high: int, length: int) -> List[int]:
    '''
    产生指定长度的随机数组
    数组中元素范围为[low, high]
    '''
    res = []
    random.seed(time.time())
    for i in range(length):
        res.append(random.randrange(low, high+1))
    return res

def createRandomStr(length: int, isCaps: int):
    '''
    length: 字符串长度

    isCaps: 1 ->  只有大写字母

    isCaps: 0 ->  大/小写字母都有

    isCaps: -1 ->  只有小写字母
    '''

    def charMap(num: int) -> int:
        '''
        num for 1~52
        '''
        if num > 26:
            return num - 26 + 96
        else:
            return num + 64
    random.seed(time.time())
    res = ""
    if isCaps == -1:
        for _ in range(length):
            res += chr(random.randrange(97, 123))
    elif isCaps == 0:
        for _ in range(length):
            res += chr(random.randrange(1, 53))
    else:
        for _ in range(length):
            res += chr(random.randrange(65, 91))
        
    return res

