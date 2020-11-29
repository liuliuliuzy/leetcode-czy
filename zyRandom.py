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