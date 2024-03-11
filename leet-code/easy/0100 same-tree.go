package leet

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}

	if p == nil && q != nil || p != nil && q == nil || p.Val != q.Val {
		return false
	}

	res := isSameTree(p.Left, q.Left)
	return isSameTree(p.Right, q.Right) && res
}
