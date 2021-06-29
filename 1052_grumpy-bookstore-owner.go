package main

import "fmt"

func maxSatisfied(customers []int, grumpy []int, X int) int {
	// O(n) 滑动窗口
	total := 0
	n := len(customers)
	for i := 0; i < n; i++ {
		if grumpy[i] == 0 {
			total += customers[i]
		}
	}
	// find the biggest increase
	increase := 0
	for i := 0; i < X; i++ {
		increase += customers[i] * grumpy[i]
	}
	maxIncrease := increase
	for i := X; i < n; i++ {
		increase = increase - customers[i-X]*grumpy[i-X] + customers[i]*grumpy[i]
		if maxIncrease < increase {
			maxIncrease = increase
		}
	}
	return total + maxIncrease
}

// sliding window
func main() {
	customers := []int{2, 3, 1, 1, 3}
	grumpys := []int{0, 1, 1, 0, 1}
	X := 2
	// fmt.Println("Hello world")
	fmt.Println("res: ", maxSatisfied(customers, grumpys, X))
}
