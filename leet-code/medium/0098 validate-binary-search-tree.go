package leet

import "math"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	return isBST(root, math.MinInt, math.MaxInt)
}

func isBST(node *TreeNode, min, max int) bool {
	if node == nil {
		return true
	}

	if node.Val < min || node.Val > max {
		return false
	}

	return isBST(node.Left, min, node.Val-1) &&
		isBST(node.Right, node.Val+1, max)
}
