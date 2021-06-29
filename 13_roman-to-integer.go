package solutions

import "fmt"

func RomanToInt(s string) int {
	return romanToInt(s)
}

func romanToInt(s string) int {
	res := 0
	length := len(s)
	for i := 0; i < length; i++ {
		switch s[i] {
		case 'I': //1
			if i+1 < length && (s[i+1] == 'V' || s[i+1] == 'X') {
				res -= 1
			} else {
				res += 1
			}
		case 'V': //5
			res += 5
		case 'X': //10
			if i+1 < length && (s[i+1] == 'L' || s[i+1] == 'C') {
				res -= 10
			} else {
				res += 10
			}
		case 'L': //50
			res += 50
		case 'C': //100
			if i+1 < length && (s[i+1] == 'D' || s[i+1] == 'M') {
				res -= 100
			} else {
				res += 100
			}
		case 'D': //500
			res += 500
		case 'M': //1000
			res += 1000
		default:
			fmt.Println("match error")
		}
	}
	return res
}
