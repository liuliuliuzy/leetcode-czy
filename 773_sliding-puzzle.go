package solutions

import (
	"strings"
)

/*
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.

一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.

最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-puzzle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

//标签：广度优先哎
func slidingPuzzle(board [][]int) int {
	//以下又是大致看一下题解，然后自己实现
	target := "123450"
	//neighbors[i]表示第i个0的邻居索引
	neighbors := [][]int{{1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4}}
	bytes := make([]byte, 0, 6)
	for _, row := range board {
		for _, col := range row {
			bytes = append(bytes, '0'+byte(col))
		}
	}
	//初始board状态对应的字符串
	start := string(bytes)
	if start == target {
		return 0
	}
	type pair struct {
		status string
		steps  int
	}
	q := []pair{{start, 0}}

	var nexts = func(now string) (res []string) {
		s := []byte(now)
		m := strings.Index(now, "0")
		for _, n := range neighbors[m] {
			s[m], s[n] = s[n], s[m]
			res = append(res, string(s))
			s[m], s[n] = s[n], s[m]
		}
		return
	}

	visited := map[string]bool{start: true}
	for len(q) > 0 {
		p := q[0]
		q = q[1:]
		// fmt.Println(nexts(p.status))
		for _, next := range nexts(p.status) {
			if !visited[next] {
				if next == target {
					return p.steps + 1
				}
				visited[next] = true
				q = append(q, pair{next, p.steps + 1})
			}
		}
	}
	return -1
}

func SlidingPuzzle(board [][]int) int {
	return slidingPuzzle(board)
}
