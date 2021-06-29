package solutions

//原地算法，删除数组中的重复元素
func removeDuplicatesE(nums []int) int {
	if len(nums) < 2 {
		return len(nums)
	}
	i, j := 1, 1
	for i < len(nums) {
		for i < len(nums) && nums[i] == nums[i-1] {
			i++
		}
		if i > j && i < len(nums) {
			nums[j] = nums[i]
		}
		if i < len(nums) {
			j++
			i++
		}
	}
	return j
}

func RemoveDuplicatesE(nums []int) int {
	return removeDuplicatesE(nums)
}
