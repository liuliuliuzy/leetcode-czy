class Solution:
    def decodeString(self, s: str) -> str:
        '''
        唯一的问题：解决编码字符串的嵌套处理
        '''
        res = ""
        specials = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']']
        st1 = []  # for number
        st2 = []  # for '['
        for i in range(len(s)):
            if s[i] not in specials:
                res += s[i]
                continue
            if s[i] == '[':
                st2.append(i)
            elif s[i] == ']':
                


        return res
if __name__ == "__main__":
    s = Solution()
    encodedString = ""
    print(s.decodeString(encodedString))