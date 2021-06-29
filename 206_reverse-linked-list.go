package solutions

//常数 空间复杂度
func reverseList(head *ListNode) *ListNode {
	var previous *ListNode = nil
	var current *ListNode = head
	for current != nil {
		next := current.Next
		current.Next = previous
		previous = current
		current = next
	}
	return previous
}

func ReverseList(head *ListNode) *ListNode {
	return reverseList(head)
}
