def isPalindrome(s)->bool:
    #method: double pointer
    # if empty
    def isCharaOrNum(k):
        if 48<=ord(k)<=57 or 65<=ord(k)<=90 or 97<=ord(k)<=122:
            return True
        return False
    
    def isEqual(s1, s2):
        if ord(s1)<=57 or ord(s2)<=57:
            return ord(s1)==ord(s2)
        else:
            return ord(s1)-ord(s2) == 0 or ord(s1)-ord(s2) == 32

    if len(s) <= 1:
        return True
    i = 0
    j = len(s)-1
    while i <= j:
        while i<j and not isCharaOrNum(s[i]):
            i+=1
        while j>i and not isCharaOrNum(s[j]):
            j-=1
        if i == len(s):
            return True
        #print(i ,j)
        if not isEqual(s[i], s[j]):
            print(s[i], s[j])
            return False
        i+=1
        j-=1
    return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))