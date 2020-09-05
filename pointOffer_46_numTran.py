# 给定一个数字，我们按照如下规则把它翻译为字符串：
# 0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，
# 25 翻译成 “z”。一个数字可能有多个翻译。
# 请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

# 示例 1:

# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，
# 分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
#  

# 提示： 0 <= num < 231

def translateNum(num: int) -> int:
    if num <= 9:
        return 1
    
    digit = []
    spaces = []
    res = 1
    while num > 0:
        digit.append(num%10)
        num = num//10
    digit.reverse()

    tmpNum = 0
    for i in range(len(digit)-1):
        if (digit[i]*10+digit[i+1]) <= 25 and digit[i]!=0:
            tmpNum += 1
        else:
            if tmpNum!=0:
                spaces.append(tmpNum)
                tmpNum = 0
    if tmpNum!=0: spaces.append(tmpNum)
    if len(spaces) == 0:
        return res
    maxNum = max(spaces)
    fn0 = [1]
    fn1 = [1]
    for i in range(1, maxNum):
        fn0.append(fn1[i-1])
        fn1.append(fn1[i-1]+fn0[i-1])
    for item in spaces:
        res *= (fn0[item-1]+fn1[item-1])
    # print(spaces)
    # print(digit)
    return res


if __name__ == "__main__":
    num = 506
    print(translateNum(num))