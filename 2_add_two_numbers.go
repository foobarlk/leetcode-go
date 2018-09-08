package leetcode

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy

	carry := 0
	for i, j := l1, l2; i != nil || j != nil; {
		sum := carry

		if i != nil {
			sum += i.Val
		}

		if j != nil {
			sum += j.Val
		}

		tail.Next = &ListNode{sum % 10, nil}
		tail = tail.Next
		carry = sum / 10

		if i != nil {
			i = i.Next
		}

		if j != nil {
			j = j.Next
		}
	}

	if carry != 0 {
		tail.Next = &ListNode{carry, nil}
	}

	return dummy.Next
}
