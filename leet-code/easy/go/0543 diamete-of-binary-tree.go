package leet

/**
* Definition for a binary tree node.
* type TreeNode struct {
*     Val int
*     Left *TreeNode
*     Right *TreeNode
* }
 */
var md int

func diameterOfBinaryTree(root *TreeNode) int {
	md = 0
	maxDepth(root)

	return md
}

func maxDepth(node *TreeNode) int {
	if node == nil {
		return 0
	}

	left := maxDepth(node.Left)
	right := maxDepth(node.Right)

	md = max(md, left+right)

	return 1 + max(left, right)
}
