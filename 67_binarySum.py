def addBinary(a, b)->str:
    res = ""
    carry = 0
    pos = 0
    lengthA = len(a)
    lengthB = len(b)
    while pos < lengthA and pos < lengthB:
        tmpSum = int(a[lengthA-1-pos])+int(b[lengthB-1-pos])+carry
        print(a[lengthA-1-pos], b[lengthB-1-pos], carry, res, tmpSum)
        if tmpSum >= 2:
            carry = 1
            res = str(tmpSum-2)+res
            # print(res)
        else:
            carry = 0
            res = str(tmpSum)+res
        pos += 1
    if pos >= lengthA:
        if carry == 0:
            res = b[0:lengthB-pos]+res
        else:
            while pos < lengthB:
                print(b[lengthB-1-pos])
                if int(b[lengthB-1-pos])+carry == 2:
                    carry = 1
                    res = "0"+res
                else:
                    res = b[0:lengthB-pos-1]+"1"+res
                    break
                pos += 1
    else:
        if carry == 0:
            res = a[0:lengthA-pos]+res
        else:
            while pos < lengthA:
                print(a[lengthA-1-pos])
                if int(a[lengthA-1-pos])+carry == 2:
                    carry = 1
                    res = "0"+res
                else:
                    carry = 0
                    res = a[0:lengthA-pos-1]+"1"+res
                    break
                pos += 1
    if carry == 1:
        res = "1"+res
    return res

def addBinaryVersion2(a, b)->str:
    if a == "0":
        return b
    if b== "0":
        return a
    lengthA = len(a)
    lengthB = len(b)
    length = max(lengthA, lengthB)
    res = ""
    pos = 0
    tmpSum = 0
    carry = 0
    aDigit = bDigit = 0
    while pos < length:
        if pos < lengthA:
            aDigit = int(a[lengthA-1-pos])
        else:
            aDigit = 0
        if pos < lengthB:
            bDigit = int(b[lengthB-1-pos])
        else:
            bDigit = 0
        tmpSum = aDigit + bDigit + carry
        carry = tmpSum//2
        res = str(tmpSum%2)+res
        pos += 1
    if carry == 1:
        res = "1"+res
    return res
if __name__ == "__main__":
    a = "101111"
    b= "10"
    print(addBinaryVersion2(a, b))