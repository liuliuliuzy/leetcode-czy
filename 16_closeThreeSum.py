def threeSumClosest(nums, target: int) -> int:
    if(not nums or len(nums) < 3):
        return None
    nums.sort()
    Sum = nums[0]+ nums[1]+nums[2]
    if (target <= Sum):
        return Sum
    dis = abs(target-Sum)
    length = len(nums)
    for i in range(length):
        L = i+1
        R = length-1
        tmp = 0
        flag = 0
        while(L < R):
            tmp = nums[i] + nums[L] + nums[R]
            if(abs(tmp - target) < dis):
                dis = abs(tmp - target)
                Sum = tmp
            if(tmp == target):
                return target
            elif(tmp > target):
                R = R-1
            else:
                L = L+1
    return Sum
if __name__ == "__main__":
    target = 11
    nums = [2,6,1,8,14]
    print(threeSumClosest(nums, target))