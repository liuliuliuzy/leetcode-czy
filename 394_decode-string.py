class Solution:
    def decodeString(self, s: str) -> str:
        '''
        唯一的问题：解决编码字符串的嵌套处理
        双栈，一个存数字，一个存待乘的字符串
        看到用栈的提示，一时没有想出来，后来居然自己想出来了，还不错(*^_^*)
        '''
        specials = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']']
        st1 = []  # for number
        st2 = [""] # for string
        
        i = 0
        while i < len(s):
            # 如果是字母
            if s[i] not in specials:
                st2[-1] += s[i]
                i += 1
                continue
            # 如果是特殊字符
            if s[i] == '[':
                st2.append("")
            elif s[i] == ']':
                tmpSt = int(st1[-1]) * st2[-1]
                st2.pop()
                st2[-1] += tmpSt
                st1.pop()
            else:
                st1.append(s[i])
                i += 1
                while 48 <= ord(s[i]) <= 57:
                    st1[-1] += s[i]
                    i += 1
                continue
            i += 1
        return st2[0]

if __name__ == "__main__":
    s = Solution()
    encodedString = "dff"
    print(s.decodeString(encodedString))