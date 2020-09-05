from typing import List

#直接调用库函数排序版本
def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort()
    return nums[len(nums)-k]

#堆排序+分治算法
def findKthLargestMy(nums: List[int], k: int)->int:
    res = 0
    
    return res
# if __name__ == "__main__":
