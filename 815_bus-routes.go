package solutions

import "math"

//广度优先吧，得先确定一个终止条件
func numBusesToDestination(routes [][]int, source int, target int) int {
	//应该将每条线路看作一个整体，进行广度优先搜索

	//如果起点就是目的地
	if source == target {
		return 0
	}

	//建图
	n := len(routes)
	edge := make([][]bool, n)
	for i := range edge {
		edge[i] = make([]bool, n)
	}
	rec := map[int][]int{}
	for i, route := range routes {
		for _, site := range route {
			for _, j := range rec[site] {
				edge[i][j] = true
				edge[j][i] = true
			}
			rec[site] = append(rec[site], i)
		}
	}
	//上述循环运行完后，应该建立起了一个无向图

	distance := make([]int, n)
	for i := range distance {
		distance[i] = -1
	}

	//进行广度优先的队列
	q := []int{}
	for _, bus := range rec[source] {
		distance[bus] = 1
		q = append(q, bus)
	}
	for len(q) > 0 {
		x := q[0]
		q = q[1:]
		for y, b := range edge[x] {
			if b && distance[y] == -1 {
				distance[y] = distance[x] + 1
				q = append(q, y)
			}
		}
	}

	ans := math.MaxInt32
	for _, bus := range rec[target] {
		if distance[bus] != -1 && distance[bus] < ans {
			ans = distance[bus]
		}
	}
	if ans < math.MaxInt32 {
		return ans
	}
	return -1
}

func isContainInt(route []int, target int) bool {
	for _, i := range route {
		if i == target {
			return true
		}
	}
	return false
}

func NumBusesToDestination(routes [][]int, source int, target int) int {
	return numBusesToDestination(routes, source, target)
}
