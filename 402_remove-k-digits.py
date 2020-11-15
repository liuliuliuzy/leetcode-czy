class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        这题乍一看想不到什么思路

        每次移除，都确保这是当前最佳方案，即可处理移除K位的问题

        那么问题变为了，如何确定当前的最佳方案（指移除一位）
        '''
            
        stack = []
        start = count = 0
        while start < len(num):
            if not stack or ord(stack[-1]) <= ord(num[start]) or count == k:
                stack.append(num[start])
                start += 1
            else:
                stack.pop()
                count += 1
        # 如果非降序，即遍历完所有位数之后并没有删除K位
        if count < k:
            stack = stack[ : (count - k)]
        print(stack)
        # 去除前导0
        while stack and stack[0] == "0":
            stack = stack[1:]
        # 如果栈为空，则返回"0"
        if not stack:
            return "0"
        return "".join(stack)


if __name__ == "__main__":
    s = Solution()
    num1 = "1432219"
    num2 = "100200"
    print(s.removeKdigits(num2, 3))
