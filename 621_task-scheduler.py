from typing import List
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCounts = collections.Counter(tasks)
        m = len(taskCounts)
        nextValidTime = [1 for i in range(m)]
        restTimes = list(taskCounts.values())
        print(nextValidTime, restTimes)
        nowTime = 0
        for i in range(len(tasks)):
            # 当前时间刻度加一
            nowTime += 1

            #找出当前任务中最早可执行时间，将当前时刻直接跳到那里
            minValidTime = min(nextValidTime[j] for j in range(m) if restTimes[j] > 0)
            nowTime = max(nowTime, minValidTime)

            # 找出可执行的并且剩余执行次数最多的任务
            bestIndex = -1
            for j in range(m):
                if nextValidTime[j] <= nowTime:
                    if bestIndex == -1 or restTimes[j] > restTimes[bestIndex]:
                        bestIndex = j
            
            #当前时刻执行该任务，因此剩余次数减一，下次可执行时间加 n+1
            restTimes[bestIndex] -= 1
            nextValidTime[bestIndex] = nowTime + n + 1

        return nowTime

if __name__ == "__main__":
    S = Solution()
    tasks = ["A","A","A","B","B","B"]
    print(S.leastInterval(tasks, 2))