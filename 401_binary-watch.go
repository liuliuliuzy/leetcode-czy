package solutions

import (
	"fmt"
	"math/bits"
)

func ReadBinaryWatch(turnedOn int) []string {
	return readBinaryWatch(turnedOn)
}

//回溯
func readBinaryWatch(turnedOn int) []string {
	res := make([]string, 0)
	//先给出定义，后面再声明
	var backtrack func(int, int, uint8, uint8)

	backtrack = func(index, ones int, hour, minute uint8) {
		if index == 10 || ones == 0 {
			if ones == 0 && hour <= 11 && minute <= 59 {
				time := ""
				// fmt.Println(hour, minute)
				time += fmt.Sprintf("%2d:%02d", int(hour), int(minute))
				//加入结果
				res = append(res, time)
			}
			return
		}
		if bits.OnesCount8(minute) == 5 {
			backtrack(6, ones, hour, minute)
			return
		}
		if bits.OnesCount8(hour) == 3 {
			backtrack(10, ones, hour, minute)
			return
		}
		if index < 6 { //0, 1, 2, 3, 4, 5
			//两种选择
			backtrack(index+1, ones-1, hour, minute|(1<<index))
			backtrack(index+1, ones, hour, minute)
		} else {
			backtrack(index+1, ones-1, hour|(1<<(index-6)), minute)
			backtrack(index+1, ones, hour, minute)
		}
	}
	if turnedOn < 9 {
		backtrack(0, turnedOn, 0, 0)
	}
	return res
}
