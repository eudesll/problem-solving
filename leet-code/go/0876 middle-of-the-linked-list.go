package leet

type ListNode struct {
	Val  int
	Next *ListNode
}

func middleNode(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	// size := 0.0
	// for cur := head; cur.Next != nil; cur = cur.Next {
	// 	size++
	// }

	// half := math.Ceil(size / 2.0)
	// for i := 0.0; i < half; i++ {
	// 	head = head.Next
	// }

	slow := head
	fast := head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	return slow
}
