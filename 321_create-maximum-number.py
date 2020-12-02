from typing import List
import zyRandom
import time
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        '''
        实际上是求两个数组的最大子序列
        '''
        def maxSub(nums: List[int], k: int) -> List[int]:
            '''
            求得nums数组中长度为k的最大子序列
            '''
            if k > len(nums):
                return None
            if k == len(nums):
                return nums
            monoStack = []
            for i in range(len(nums)):
                if len(nums) - i > k - len(monoStack):
                    while monoStack and monoStack[-1] < nums[i] and len(nums) - i > k - len(monoStack):
                        monoStack.pop()
                    if len(monoStack) < k:
                        monoStack.append(nums[i])
                else:
                    monoStack.extend(nums[i:])
                    break
            return monoStack
        
        def compare(n1: List[int], index1: int, n2:List[int], index2: int) -> int:
            tm, tn = len(n1), len(n2)
            while index1 < tm and index2 < tn:
                if n1[index1] != n2[index2]:
                    return n1[index1] - n2[index2]
                index1 += 1
                index2 += 1
            return tm - index1 - (tn - index2)

        m, n = len(nums1), len(nums2)
        k1 = 0
        res = []
        if k > n:
            k1 = k - n
        for i in range(k1, m+1):
            res1 = maxSub(nums1, i) # k1
            res2 = maxSub(nums2, k - i) # k2
            # merge
            tmpres = []
            u, d = 0, 0
            print(i, k-i, res1, res2)
            for _ in range(k):
                if compare(res1, u, res2, d) > 0:
                    tmpres.append(res1[u])
                    u += 1
                else:
                    tmpres.append(res2[d])
                    d += 1
                print(u, d)
            
            for t in range(k):
                if t >= len(res) or res[t] < tmpres[t]:
                    res = tmpres[:]
                    break
                if res[t] > tmpres[t]:
                    break
            print("got tmpres:", tmpres, "res1:", res1, "res2", res2, "now res:", res)
        return res

if __name__ == "__main__":
    S = Solution()
    nums1 = [8,6,9]
    nums2 = [1,7,5]
    # nums1 = zyRandom.createRandList(1, 9, 4)
    # time.sleep(2)
    # nums2 = zyRandom.createRandList(1, 9, 7)
    # print("nums1:", nums1, "nums2:", nums2)
    # for i in range(12):
    print(S.maxNumber(nums1, nums2, 3))
            