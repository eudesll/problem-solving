package leet

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	cur := head

	var recursive func(*ListNode) bool
	recursive = func(node *ListNode) bool {
		if node == nil {
			return true
		}

		nextResults := recursive(node.Next)

		value := cur.Val
		cur = cur.Next

		return value == node.Val && nextResults
	}

	return recursive(head)
}
