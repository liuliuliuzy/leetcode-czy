package solutions

import "fmt"

//题目：
// 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 m * n 的网格 grid 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 0。

// 为了使收益最大化，矿工需要按以下规则来开采黄金：

// 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
// 矿工每次可以从当前位置向上下左右四个方向走。
// 每个单元格只能被开采（进入）一次。
// 不得开采（进入）黄金数目为 0 的单元格。
// 矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/path-with-maximum-gold
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

func GetMaximumGold(grid [][]int) int {
	return getMaximumGold(grid)
}

// 回溯算法
func getMaximumGold(grid [][]int) int {
	res := 0
	m := len(grid)
	n := len(grid[0])
	var backtrack func(int, int, int, [][]bool)
	backtrack = func(i, j, sum int, visited [][]bool) {
		//终止条件
		if i < 0 || i > m-1 || j < 0 || j > n-1 || grid[i][j] == 0 || visited[i][j] {
			return
		}
		visited[i][j] = true
		sum += grid[i][j]
		if sum > res {
			res = sum
		}
		backtrack(i-1, j, sum, visited)
		backtrack(i+1, j, sum, visited)
		backtrack(i, j+1, sum, visited)
		backtrack(i, j-1, sum, visited)
		// 思考一下为什么这里要将visited改回false
		visited[i][j] = false
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				continue
			}
			// 创建visited slice记录走过的点
			visited := make([][]bool, m)
			for k := range visited {
				visited[k] = make([]bool, n)
			}
			fmt.Printf("%T\n", visited)
			fmt.Println(visited)
			backtrack(i, j, 0, visited)
		}
	}

	return res
}
