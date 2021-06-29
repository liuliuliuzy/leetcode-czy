package solutions

func removeDuplicates(nums []int) int {
	res := 1
	i := 1
	// nowNum = nums[0]
	flag := -1
	for i < len(nums) {

		if flag < 0 {
			// fmt.Println(res, i)
			nums[res] = nums[i]
		} else {
			j := i + 1
			for j < len(nums) && nums[j] == nums[i] {
				j += 1
			}
			i = j
			flag = -1
			continue
			// fmt.Println(i)
		}
		// modify flag
		if nums[i] == nums[i-1] {
			flag += 1
		} else {
			flag = -1
		}
		res += 1
		i += 1
		// fmt.Println(res, i, nums, flag)
	}
	return res
}

func RemoveDuplicates(nums []int) int {
	return removeDuplicates(nums)
}
