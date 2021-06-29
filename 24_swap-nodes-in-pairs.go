package solutions

//两两翻转链表，递归
func swapPairs(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	t1 := head
	t2 := head.Next.Next
	head = head.Next
	head.Next = t1
	t1.Next = swapPairs(t2)
	return head
}

func SwapPairs(head *ListNode) *ListNode {
	return swapPairs(head)
}
