package solutions

import "goleetcode/mylibs"

func StoneGame(piles []int) bool {
	return stoneGame(piles)
}

// 又是这种决策型的题目
// 下面抄的官方题解
func stoneGame(piles []int) bool {
	length := len(piles)
	dp := make([][]int, length)
	for i := 0; i < length; i++ {
		dp[i] = make([]int, length)
		dp[i][i] = piles[i]
	}
	for i := length - 2; i >= 0; i-- {
		for j := i + 1; j < length; j++ {
			dp[i][j] = mylibs.Max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
		}
	}
	return dp[0][length-1] > 0
}
