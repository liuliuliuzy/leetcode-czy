package solutions

import "fmt"

func canMeasureWater(jug1Capacity int, jug2Capacity int, targetCapacity int) bool {
	//等价于最大公约数问题
	if targetCapacity > jug1Capacity+jug2Capacity {
		return false
	}

	if jug1Capacity*jug2Capacity == 0 {
		return targetCapacity == jug1Capacity+jug2Capacity
	}
	m := jug1Capacity % jug2Capacity
	//辗转相除求最大公约数
	for m > 0 {
		jug1Capacity = jug2Capacity
		jug2Capacity = m
		m = jug1Capacity % jug2Capacity
	}
	fmt.Println(jug2Capacity)
	return targetCapacity%jug2Capacity == 0
}

func CanMeasureWater(jug1Capacity int, jug2Capacity int, targetCapacity int) bool {
	return canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)
}
