package solutions

func removeElement(nums []int, val int) int {
	i, j := 0, 0
	for i < len(nums) {
		for i < len(nums) && nums[i] == val {
			i++
		}
		if i < len(nums) {
			nums[j] = nums[i]
			j++
			i++
		}
	}
	return j
}

func RemoveElement(nums []int, val int) int {
	return removeElement(nums, val)
}
