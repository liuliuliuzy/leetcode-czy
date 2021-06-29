package solutions

import "fmt"

func LongestPalindrome(s string) int {
	return longestPalindrome(s)
}

//hash table solves it
func longestPalindrome(s string) int {
	ht := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		ht[s[i]]++
	}
	offSet := 0
	res := 0
	fmt.Println(ht)
	for _, value := range ht {
		if value%2 == 1 {
			res += (value - offSet)
			offSet = 1
		} else {
			res += value
		}
	}
	return res
}
