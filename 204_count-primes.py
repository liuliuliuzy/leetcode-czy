import math

class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        计算小于n的质数的个数
        n输入最大有5*10^6，数学题？
        '''
        # 暴力枚举，看会不会超时--用python写果然超时了^=^，C++也超时了^.^
        def judgeOne(num: int) -> bool:
            '''
            True: prime\n
            False: not prime
            '''
            for i in range(2, math.floor(math.sqrt(num) + 1) ):
                if num % i == 0:
                    return False
            return True

        res = 0
        for i in range(2, n):
            if judgeOne(i):
                print(i)
                res += 1
        
        return res
    
    def countPrimesII(self, n: int) -> int:
        '''
        埃氏筛选法
        '''
        isPrime = [True for i in range(n)]
        res = 0
        for j in range(2, n):
            if isPrime[j]:
                res += 1
                print(j)
                tmp = j * j
                while tmp < n:
                    isPrime[tmp] = False
                    tmp += j
        
        return res

    def countPrimesIII(self, n: int) -> int:
        '''
        线性筛选法
        '''
        primes = []
        isPrime = [True for i in range(n)]
        for i in range(2, n):
            if isPrime[i]:
                primes.append(i)
            j = 0
            while j < len(primes) and i * primes[j] < n:
                isPrime[i * primes[j]] = False
                if i % primes[j] == 0:
                    break                
                j += 1
        # print(primes)
        return len(primes)




if __name__ == "__main__":
    S = Solution()
    print(S.countPrimesIII(999983))