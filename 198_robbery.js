/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if(nums.length==0){
        return 0
    }
    if(nums.length < 3){
        return Math.max(...nums)
    }
    var Xn = Math.max(nums[0], nums[1])
    var Xn_1 = nums[0]
    var ans = 0
    for(let i=2; i<nums.length; i++){
        ans = Math.max(Xn, Xn_1+nums[i])
        Xn_1 = Xn
        Xn = ans
    }
    return ans
};

var nums = [3]
console.log(rob(nums))