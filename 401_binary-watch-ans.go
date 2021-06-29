package solutions

import "fmt"

func ReadBinaryWatchII(num int) []string {
	res := []string{}
	// 假想 10个 bit 灯 index  --->       h1=>0   h2=>1   h4=>2   h8=>3   m1=>4   m2=>5   m4=>6   m8=>7   m16=>8   m32=>9
	//start = 0 回溯从bit 的 index = 0 开始, 10 代表时分灯的总数, 相当于10个灯中选中num个亮的灯
	backTrack(0, 10, num, []int{}, &res)
	return res
}

//backTrack 回溯算法
//cap 灯的总数量
//target 目标亮灯的数量
//path []int  亮灯的index集合(记录回溯的路径)
//res 指针返回结果
func backTrack(start, cap, target int, path []int, res *[]string) {
	if len(path) == target { //选择亮灯的数量达到target
		min, hour := 0, 0
		for _, v := range path {
			if v >= 4 { // 如果灯的下表超过3 则表示这些灯是 minute的灯
				min += 1 << (v - 4)
			} else { //如果 灯的index 小于4 表示是 hour的灯亮
				hour += 1 << v
			}
		}
		if min < 60 && hour < 12 { //排除不符合规则的,判断min hour 值是否有效
			*res = append(*res, fmt.Sprintf("%d:%02d", hour, min)) //格式化拼接成字符串
		}
		return
	}
	for i := start; i < cap; i++ {
		path = append(path, i)
		backTrack(i+1, cap, target, path, res) //注意这里是 i+1
		path = path[:len(path)-1]              //对 path 进行rollback
	}
}
