package solutions

import (
	"fmt"
)

/**
 * Definition for singly-linked list.
 */
type ListNode struct {
	Val  int
	Next *ListNode
}

//合并有序链表 空指针：nil
//最简单的思路，创建新链表，往后加节点
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	var res *ListNode = &ListNode{}
	var tmp = res
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			tmp.Next = &ListNode{
				Val:  l1.Val,
				Next: nil,
			}
			l1 = l1.Next
		} else {
			tmp.Next = &ListNode{
				Val:  l2.Val,
				Next: nil,
			}
			l2 = l2.Next
		}
		tmp = tmp.Next
	}
	if l1 != nil {
		for l1 != nil {
			tmp.Next = &ListNode{
				Val:  l1.Val,
				Next: nil,
			}
			tmp = tmp.Next
			l1 = l1.Next
		}
	} else {
		for l2 != nil {
			tmp.Next = &ListNode{
				Val:  l2.Val,
				Next: nil,
			}
			tmp = tmp.Next
			l2 = l2.Next
		}
	}
	return res.Next
}

func MergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	return mergeTwoLists(l1, l2)
}

func PrintLinkedList(head *ListNode) {
	fmt.Printf("%s ", "[")
	for head != nil {
		fmt.Printf("%d -> ", head.Val)
		head = head.Next
	}
	fmt.Printf("%s\n", "nil ]")
}

//递归解法
func mergeTwoListsRec(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	} else {
		if l1.Val < l2.Val {
			l1.Next = mergeTwoListsRec(l1.Next, l2)
			return l1
		} else {
			l2.Next = mergeTwoListsRec(l1, l2.Next)
			return l2
		}
	}
}

func MergeTwoListsRec(l1 *ListNode, l2 *ListNode) *ListNode {
	return mergeTwoListsRec(l1, l2)
}
