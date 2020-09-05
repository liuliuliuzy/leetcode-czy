
def isPalindrome(x: int) -> bool:
    if x < 0: return False
    s =str(x)
    # print(s)
    # digits = []
    # while x > 0:
    #     digits.append(x%10)
    #     x = x//10
    # if not digits: return True
    if len(s) == 1: return True
    for i in range((len(s)+1)//2):
        if s[i]!=s[len(s)-1-i]:
            return False
    return True

# 如果不把数字转换为字符串
# 思路：反转数字，为了避免反转后溢出的情况，可以反转一半数字
def isPalindromeV2(x: int)->bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    revertedNumber = 0
    while x > revertedNumber:
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10
    return x == revertedNumber or x == revertedNumber // 10
    return True

if __name__ == "__main__":
    num = 161
    print(isPalindrome(num))