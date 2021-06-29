package solutions

import "goleetcode/mylibs"

//几何、数学、哈希表？
//我本来以为有什么O(n^2)以内的方法，没想到题解一上来就是暴力
func maxPoints(points [][]int) int {
	//直接双重循环
	if len(points) < 3 {
		return len(points)
	}
	res := 0
	for i := 0; i < len(points)-1; i++ {
		//已经无法得到更大的答案了
		if len(points)-i < res {
			break
		}
		//记录的哈希表应该在一重循环里面创建
		counts := make(map[[2]int]int)
		for j := i + 1; j < len(points); j++ {
			//计算points[i]与其它点的斜率
			deltaX := points[i][0] - points[j][0]
			deltaY := points[i][1] - points[j][1]
			if deltaX*deltaY == 0 {
				if deltaX == 0 {
					deltaY = 1
				} else {
					deltaX = 0
				}
			} else {
				absX := deltaX
				absY := deltaY
				if deltaX < 0 {
					absX = -1 * absX
				}
				if deltaY < 0 {
					absY = -1 * absY
				}
				gcd := mylibs.Gcd(absX, absY)
				if gcd > 1 {
					deltaX = deltaX / gcd
					deltaY = deltaY / gcd
				}
				if deltaX < 0 {
					deltaX = -1 * deltaX
					deltaY = -1 * deltaY
				}
			}
			counts[[2]int{deltaX, deltaY}] += 1
			if res < counts[[2]int{deltaX, deltaY}] {
				res = counts[[2]int{deltaX, deltaY}]
			}
		}
	}
	return res + 1
}

func MaxPoints(points [][]int) int {
	return maxPoints(points)
}
