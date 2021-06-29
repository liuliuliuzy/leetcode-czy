package solutions

func hammingWeight(num uint32) int {
	res := 0
	for i := 0; i < 32; i++ {
		if num&(uint32(1<<i)) > 0 {
			res += 1
		}
	}
	return res
}

func HammingWeight(num uint32) int {
	return hammingWeight(num)
}
