def patternMatch(pattern: str, value: str)->bool:
    # if pattern in ["a", "b", "ab", "ba"]: return True
    count_a = count_b = 0
    for ch in pattern:
        if ch == 'a':
            count_a += 1
        else:
            count_b += 1
    if count_a < count_b:
        count_a, count_b = count_b, count_a
        pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)

    #处理特殊情况
    if len(pattern) == 0:
        return value == ""
    if count_b == 0:
        if len(value)%count_a != 0:
            return False
        else:
            pattern_len = int(len(value)/count_a)
            pos = 0
            pattern = ""
            pattern_count = 0
            tmps = ""
            while pos < len(value):
                for j in range(pattern_len):
                    tmps += value[pos]
                    pos += 1
                if pattern_count == 0:
                    pattern = tmps
                else:
                    if tmps!=pattern: return False
                tmps = ""
                pattern_count += 1
            return True
    if len(value) == 0:
        return count_b == 0
    for i in range( (len(value)//count_a)+1 ):
        if (len(value) - count_a*i)%count_b != 0:
            continue
        a_pattern_len = i
        b_pattern_len = int((len(value)-count_a*i)/count_b)
        a_pattern = ""
        b_pattern = ""
        pos_value = 0
        pos_pattern = 0
        count = 0
        a_pattern_count = 0
        b_pattern_count = 0
        tmp_s = ""
        isMatch = True
        # print(a_pattern_len, b_pattern_len)
        while pos_value < len(value):
            if pattern[pos_pattern] == 'a':
                #取对应长度的字符串
                for j in range(a_pattern_len):
                    tmp_s += value[pos_value]
                    pos_value += 1
                #如果是第一次遇到a，那么给a赋值
                if a_pattern_count == 0:
                    a_pattern = tmp_s
                #如果不是第一次，那么判断其是否相等
                else:
                    if tmp_s != a_pattern:
                        isMatch = False
                        break
                tmp_s = ""
                a_pattern_count += 1
            else:
                #取对应长度的字符串
                for j in range(b_pattern_len):
                    tmp_s += value[pos_value]
                    pos_value += 1
                if b_pattern_count == 0:
                    b_pattern = tmp_s
                    tmp_s == ""
                else:
                    if tmp_s != b_pattern: 
                        isMatch = False
                        break
                    b_pattern_count += 1
                tmp_s = ""
                b_pattern_count += 1
            pos_pattern += 1
            # print(pos_value, "\""+a_pattern+"\"", "\""+b_pattern+"\"")
        if not isMatch:
            continue
        if a_pattern != b_pattern: 
            print("\""+a_pattern+"\"", a_pattern_len, "\""+b_pattern+"\"", b_pattern_len)
            return True
    #遍历完了所有可能，而没有匹配的情况，那么返回False
    return False

if __name__ == "__main__":
    p = "abba" 
    s = "dogcatcatfis"
    # s = ""
    print(patternMatch(p, s))