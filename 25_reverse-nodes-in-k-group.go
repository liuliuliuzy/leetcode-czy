package solutions

//从第一个开始，不断地翻转
func reverseKGroup(head *ListNode, k int) *ListNode {
	//其实O(k)空间复杂度很好做
	count := 0
	tmp := head
	//判断长度是否大于等于k
	for tmp != nil && count < k {
		tmp = tmp.Next
		count++
	}
	if count < k {
		return head
	}
	nodes := make([]*ListNode, 0)
	help := head
	count = 0
	for count < k-1 {
		nodes = append(nodes, help)
		help = help.Next
		count++
	}
	head = help
	nodes = append(nodes, help.Next)
	for count > 0 {
		help.Next = nodes[count-1]
		help = help.Next
		count--
	}
	help.Next = reverseKGroup(nodes[k-1], k)
	return head
}

func ReverseKGroup(head *ListNode, k int) *ListNode {
	return reverseKGroup(head, k)
}
