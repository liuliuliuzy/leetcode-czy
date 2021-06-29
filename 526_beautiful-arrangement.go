package solutions

func CountArrangement(n int) int {
	return countArrangement(n)
}

//回溯，筛选结果
func countArrangement(n int) int {
	res := 0
	//used[i] 表示i+1是否被使用
	used := make([]bool, n+1)

	var backTrack func(int)
	backTrack = func(index int) {
		if index > n {
			res += 1
		}
		for i := 1; i <= n; i++ {
			if !used[i] && (i%index == 0 || index%i == 0) {
				used[i] = true
				backTrack(index + 1)
				used[i] = false
			}
		}
	}
	backTrack(1)
	return res
}
