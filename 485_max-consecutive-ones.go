package solutions

func findMaxConsecutiveOnes(nums []int) int {
	res := 0
	tmp := 0
	for _, num := range nums {
		if num == 1 {
			tmp++
		} else {
			if tmp > res {
				res = tmp
			}
			tmp = 0
		}
	}
	if tmp > res {
		res = tmp
	}
	return res
}

func FindMaxConsecutiveOnes(nums []int) int {
	return findMaxConsecutiveOnes(nums)
}
