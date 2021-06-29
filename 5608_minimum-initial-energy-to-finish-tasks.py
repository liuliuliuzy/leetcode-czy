from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        init = tasks[0][1] - tasks[0][0]
        index = 0
        for i in range(1, len(tasks)):
            if tasks[i][1] - tasks[i][0] < init:
                init = tasks[i][1] - tasks[i][0]
                index = i
        res = tasks[index][1]
        del tasks[index]
        tasks.sort(key=lambda x: x[1] - x[0])
        print(tasks)
        while tasks:
            for i in range(len(tasks)):
                if res + tasks[i][0] >= tasks[i][1]:
                    res = res + tasks[i][0]
                    del tasks[i]
                    break
                else:
                    if i == len(tasks) - 1:
                        res = tasks[0][1]
                        del tasks[0]

            # res = max(res + tasks[i][0], tasks[i][1])
            # print(res)
        return res

    def minimumEffortII(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        res = 0
        while tasks:
            for i in range(len(tasks)):
                if res + tasks[i][0] >= tasks[i][1]:
                    res = res + tasks[i][0]
                    del tasks[i]
                    break
                else:
                    if i == len(tasks) - 1:
                        res = tasks[0][1]
                        del tasks[0]

        return res


if __name__ == "__main__":
    test = [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]
    s = Solution()
    print(s.minimumEffortII(test))
