package solutions

import (
	"fmt"
	"goleetcode/mylibs"
	"math/bits"
)

//过程：说实话，不看题解一时之间没有任何思路
func MaxLength(arr []string) int {
	return maxLength(arr)
}

//以下为根据题解思路，自己go语言实现
func maxLength(arr []string) int {
	//第一步：遍历arr，获得二进制数字的数组
	arrSlice := make([]uint32, 0, len(arr))
	res := 0
	for _, str := range arr {
		var strNum uint32 = 0
		for i := 0; i < len(str); i++ {
			//如果字符串中存在重复字符
			if strNum&(uint32(1<<(str[i]-0x61))) > 0 {
				strNum = 0
				break
			}
			strNum = strNum | (1 << uint32(str[i]-0x61))
		}
		// fmt.Printf("%032b\n", strNum)
		if strNum != 0 && !mylibs.IsContain(arrSlice, strNum) {
			arrSlice = append(arrSlice, strNum)
		}
	}
	// fmt.Println(arrSlice)
	var backtrack func(int, uint32)
	backtrack = func(index int, mask uint32) {
		if index == len(arrSlice) {
			fmt.Println(res, bits.OnesCount32(mask))
			res = mylibs.Max(res, bits.OnesCount32(mask))
			return
		}
		//回溯法的精髓在于，两条路都走
		//如果这里写成 if else 就不对了
		if mask&arrSlice[index] == 0 {
			backtrack(index+1, mask|arrSlice[index])
		}
		backtrack(index+1, mask)
	}
	backtrack(0, 0)
	return res
}
