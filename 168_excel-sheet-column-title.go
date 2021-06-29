package solutions

//26进制转换
func convertToTitle(columnNumber int) string {
	//数字与ASCII转换
	res := ""
	for columnNumber > 26 {
		digit := columnNumber % 26
		columnNumber = columnNumber / 26
		if digit > 0 {
			res = string([]byte{byte(digit + 64)}) + res
		} else {
			columnNumber -= 1
			res = string([]byte{byte(90)}) + res
		}
	}
	res = string([]byte{byte(columnNumber + 64)}) + res
	return res
}

func ConvertToTitle(columnNumber int) string {
	return convertToTitle(columnNumber)
}
