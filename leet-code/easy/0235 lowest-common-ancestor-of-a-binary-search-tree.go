package leet

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}

	leftCheck := lowestCommonAncestor(root.Left, p, q)
	rightCheck := lowestCommonAncestor(root.Right, p, q)

	if leftCheck != nil && rightCheck != nil ||
		root.Val == p.Val || root.Val == q.Val {
		return root
	}

	if leftCheck == nil && rightCheck != nil {
		return rightCheck
	}

	return leftCheck
}
