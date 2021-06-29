package solutions

func PeakIndexInMountainArray(arr []int) int {
	return peakIndexInMountainArray(arr)
}

/*返回山脉数组的峰顶元素索引*/
//最先想到：二分？
func peakIndexInMountainArray(arr []int) int {
	start := 0
	end := len(arr)
	mid := (start + end) / 2
	for {
		// fmt.Println(start, end, mid)
		if arr[mid-1] > arr[mid] {
			end = mid
			mid = (start + end) / 2
			continue
		}
		if arr[mid+1] > arr[mid] {
			start = mid
			mid = (start + end) / 2
			continue
		}
		break
	}
	return mid
}
