class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        字符串分割、栈的使用
        '''
        items = path.split('/')
        stack = []
        for item in items:
            if item == '.' or item == '':
                continue
            if item == '..':
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(item)
        return '/'+'/'.join(stack)

if __name__ == "__main__":
    S = Solution()
    path = '/a/./b/../../c/'
    print(S.simplifyPath(path))