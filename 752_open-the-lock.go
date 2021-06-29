package solutions

//感觉本质上和走方格是一样的
//4位数字
//广度优先
//一层层往外走
func openLock(deadends []string, target string) int {
	//记录deadends
	hash := make(map[string]bool)
	for _, item := range deadends {
		hash[item] = true
	}

	type pair struct {
		point string
		steps int
	}

	get := func(status string) (ret []string) {
		s := []byte(status)
		for i, b := range s {
			s[i] = b - 1
			if s[i] < '0' {
				s[i] = '9'
			}
			ret = append(ret, string(s))
			s[i] = b + 1
			if s[i] > '9' {
				s[i] = '0'
			}
			ret = append(ret, string(s))
			s[i] = b
		}
		return
	}

	//几种特殊情况
	if hash["0000"] {
		return -1
	}

	start := "0000"
	if start == target {
		return -1
	}
	points := make([]pair, 0)
	points = append(points, pair{start, 0})
	visited := make(map[string]bool)
	for len(points) > 0 {
		//遍历start走一步可以到达的点
		nowPointPair := points[0]
		points = points[1:]
		for _, p := range get(nowPointPair.point) {
			//如果没有走过，并且不是deadend
			if !visited[p] && !hash[p] {
				if p == target {
					return nowPointPair.steps + 1
				} else {
					visited[p] = true
					points = append(points, pair{p, nowPointPair.steps + 1})
				}
			}
		}
	}
	return -1
}

func OpenLock(deadends []string, target string) int {
	return openLock(deadends, target)
}
