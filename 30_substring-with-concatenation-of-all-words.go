package solutions

import "reflect"

// use hash table and sliding window
func findSubstring(s string, words []string) []int {
	res := make([]int, 0)
	if len(s) == 0 || len(words) == 0 {
		return res
	}
	words_ht := make(map[string]int)
	// establish hash table
	for _, item := range words {
		words_ht[item] += 1
	}
	// fmt.Print(words_ht)
	one_word := len(words[0])
	total_len := len(words) * one_word
	for i := 0; i <= len(s)-total_len; i++ {
		tmp_s := s[i : i+total_len]
		tmp_ht := make(map[string]int)
		for j := 0; j < total_len; j += one_word {
			tmp_ht[tmp_s[j:j+one_word]] += 1
		}
		if reflect.DeepEqual(words_ht, tmp_ht) {
			res = append(res, i)
		}
		// fmt.Println(tmp_s)
	}
	return res
}

func FindSubstring(s string, words []string) []int {
	return findSubstring(s, words)
}
