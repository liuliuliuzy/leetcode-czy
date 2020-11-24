from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        '''
        收一下心，开始遨游在学习的世界里了
        '''
        if len(arr) < 3 or arr[0] >= arr[1] or arr[-1] >= arr[-2]:
            return False
        
        flag = True
        for i in range(1, len(arr)-1):
            if flag:
                if arr[i] < arr[i+1]:
                    continue
                else:
                    flag = False
            else:
                if arr[i] > arr[i+1]:
                    continue
                else:
                    return False
        
        return True

            

