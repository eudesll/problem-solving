package leet

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	nodes := map[*ListNode]bool{}

	for ; head != nil; head = head.Next {
		if nodes[head] {
			return head
		}

		nodes[head] = true
	}

	return head
}
