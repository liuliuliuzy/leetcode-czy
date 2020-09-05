def reverse(x)->int:
    c = 1
    res = 0
    digits = []
    intMax = 2147483648
    limit = intMax-1
    if x < 0:
        c = -1
        x = -1*x
        limit = intMax
    while x > 0:
        digits.append(x%10)
        x = x//10
    # print(digits)
    for num in digits:
        res = res*10 + num
        if res > limit:
            return 0
    res = c*res
    return res

if __name__ == "__main__":
    x = 2147483648
    print(reverse(x))