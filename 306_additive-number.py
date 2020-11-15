from math import ceil

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        '''
        看了一下评论，好像这题挺烦的，但是我今天一定要写出来
        '''
        # def strAdd(a: str, b: str) -> str:
        #    '''
        #    字符串数字加法
        #    '''
        #    if len(a) < len(b):
        #        a, b = b, a
        #     # 假设a的长度更长
        def check(a: int, b: int) -> bool:
            a1 = int(num[0:a])
            a2 = int(num[a:b])
            nextNum = str(a1 + a2)
            nowIndex = b
            while nowIndex < n:
                if num[nowIndex: nowIndex + len(nextNum)] != nextNum:
                    return False
                nowIndex += len(nextNum)
                tmp = int(nextNum)
                nextNum = str(int(nextNum)+a2)
                a2 = tmp
            return True
                
        # flag = False
        n = len(num)
        if n < 3:
            return False
        # if num[0] == "0":

        for i in range(2, n-ceil(n/3)+1):
            for j in range(1, i):
                # 如果第二个数只有一位，那么0也可以
                # if i - j == 1:
                #     if check(j, i):
                #         return True
                # else:
                #     # 前导0要跳过
                #     if num[j] == "0":
                #         continue
                #     if check(j, i):
                #         return True
                if (i - j > 1 and num[j] == "0") or (j > 1 and num[0] == "0"):
                    continue
                if check(j, i):
                    return True

        return False
        # return check(1, 3)

if __name__ == "__main__":
    s = Solution()
    testStr = "02358"
    print(s.isAdditiveNumber(testStr))

            