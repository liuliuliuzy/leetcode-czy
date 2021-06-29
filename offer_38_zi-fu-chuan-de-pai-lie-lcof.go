package solutions

import "sort"

func Permutation(s string) []string {
	return permutation(s)
}

//简单的回溯
//考虑到s中可能有重复字符，所以不能简单地遍历每个字符然后选择是否使用

//======超时版本========
// func permutation(s string) []string {
// 	visited := make([]bool, len(s))
// 	res := make([]string, 0)
// 	var backtrack func(int, string)
// 	backtrack = func(pos int, path string) {
// 		if pos == len(s) {
// 			if !isStringIn(res, path) {
// 				res = append(res, path)
// 			}
// 		}
// 		for i := 0; i < len(s); i++ {
// 			if !visited[i] {
// 				visited[i] = true
// 				backtrack(pos+1, path+string(s[i]))
// 				visited[i] = false
// 			}
// 		}
// 	}
// 	backtrack(0, "")
// 	return res
// }

// func isStringIn(lists []string, item string) bool {
// 	for _, i := range lists {
// 		if i == item {
// 			return true
// 		}
// 	}
// 	return false
// }

func permutation(s string) []string {
	mp := make(map[string]int)
	var res []string = []string{}
	for _, ch := range s {
		mp[string(ch)] += 1
	}
	keys := make([]string, 0)
	for k := range mp {
		keys = append(keys, k)
	}
	sort.Strings(keys)
	var backtrack func(int, string)
	backtrack = func(pos int, path string) {
		if pos == len(s) {
			res = append(res, path)
			return
		}
		for i := 0; i < len(keys); i++ {
			if mp[keys[i]] > 0 {
				mp[keys[i]] -= 1
				backtrack(pos+1, path+keys[i])
				mp[keys[i]] += 1
			}
		}
	}
	backtrack(0, "")
	return res
}
