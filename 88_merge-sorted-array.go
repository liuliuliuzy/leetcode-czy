package solutions

//感觉 似乎可以原地算法？
func merge(nums1 []int, m int, nums2 []int, n int) {
	res := make([]int, m+n)
	i, j, s := 0, 0, 0
	for {
		if i > m-1 || j > n-1 {
			break
		}
		if nums1[i] < nums2[j] {
			res[s] = nums1[i]
			i += 1
		} else {
			res[s] = nums2[j]
			j += 1
		}
		s += 1
	}
	if i > m-1 {
		for j < n {
			res[s] = nums2[j]
			j += 1
			s += 1
		}
	} else {
		for i < m {
			res[s] = nums1[i]
			i += 1
			s += 1
		}
	}
	copy(nums1, res)
}

func Merge(nums1 []int, m int, nums2 []int, n int) {
	merge(nums1, m, nums2, n)
}
