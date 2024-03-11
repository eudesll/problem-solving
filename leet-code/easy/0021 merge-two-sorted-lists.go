package leet

// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil {
		return list2
	}

	s := list1
	b := list2

	if b != nil && s.Val > b.Val {
		tmp := *s
		s = b
		b = &tmp
	}

	for cur := s; b != nil && cur != nil; cur = cur.Next {
		if cur.Next == nil || b.Val < cur.Next.Val {
			tmp := *b
			b = cur.Next
			cur.Next = &tmp
		}
	}

	return s
}
