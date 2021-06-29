package solutions

import "fmt"

func guess(num int, pick int) int {
	if num > pick {
		return -1
	} else {
		if num < pick {
			return 1
		} else {
			return 0
		}
	}
}

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
	low := 1
	high := n
	myGuess := (low + high) / 2
	guessRes := guess(myGuess, 2)
	for guessRes != 0 {
		fmt.Println(guessRes, low, high, myGuess)
		if guessRes == 1 {
			low = myGuess + 1
		} else {
			high = myGuess - 1
		}
		myGuess = (low + high) / 2
		guessRes = guess(myGuess, 2)
	}
	return myGuess
}

func GuessNumber(n int) int {
	return guessNumber(n)
}
