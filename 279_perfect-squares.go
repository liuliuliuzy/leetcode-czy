package solutions

import (
	"math"
)

// leetcode - 279
// 递归是不是铁超时啊(*^_^*)
// 直接dp
func numSquares(n int) int {
	f := make([]int, n+1)
	for i := 1; i <= n; i++ {
		minn := math.MaxInt32
		for j := 1; j*j <= i; j++ {
			if minn > f[i-j*j] {
				minn = f[i-j*j]
			}
		}
		f[i] = minn + 1
	}
	return f[n]
}

func NumSquares(n int) int {
	return numSquares(n)
}
