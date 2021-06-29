package solutions

//needle为空时返回0
func strStr(haystack string, needle string) int {
	if needle == "" {
		return 0
	}
	m := len(haystack)
	n := len(needle)

	if m < n {
		return -1
	}
	for i := 0; i < m-n+1; i++ {
		if haystack[i] == needle[0] {
			j := 0
			for j < n {
				if haystack[i+j] != needle[j] {
					break
				}
				j++
			}
			if j == n {
				return i
			}
		}
	}
	return -1
}

func StrStr(haystack string, needle string) int {
	return strStr(haystack, needle)
}
