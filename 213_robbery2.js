/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    function robOne(nums) {
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
    }
    if(nums.length < 4){
        if(nums.length == 0){
            return 0
        }
        return Math.max(...nums)
    }
    return Math.max(nums[nums.length-1]+robOne(nums.slice(1, nums.length-2)), robOne(nums.slice(0, nums.length-1)))
}

var robOpti = function(nums) {

}
var houses = [1,2,3,1]
console.log(rob(houses))