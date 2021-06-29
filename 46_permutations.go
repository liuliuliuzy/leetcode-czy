package solutions

func permute(nums []int) [][]int {
	n := len(nums)
	used := make([]bool, n)
	res := make([][]int, 0)
	var fs func(int, []int)
	fs = func(pos int, path []int) {
		if pos == n {
			res = append(res, path)
		}
		//可用选择，从索引0开始
		for i := 0; i < n; i++ {
			if !used[i] {
				used[i] = true
				fs(pos+1, append(path, nums[i]))
				used[i] = false
			}
		}
	}

	path := make([]int, 0)
	fs(0, path)
	return res
}

func Permute(nums []int) [][]int {
	return permute(nums)
}
