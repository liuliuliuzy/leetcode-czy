//dynamic programming
var test = function(nums) {
    var maxSum = nums[0]
    var backMaxSum = nums[0]
    // var ans = 0
    var subArrays = [nums[0]]
    for(let i=1, len = nums.length; i<len; i++){
        backMaxSum = backMaxSum < 0 ? nums[i] : backMaxSum+nums[i]
        maxSum = maxSum > backMaxSum ? maxSum : backMaxSum
    }
    return maxSum
}
var nums = [-2,1,-3,4,-1,2,1,-5,4]
console.log(test(nums))