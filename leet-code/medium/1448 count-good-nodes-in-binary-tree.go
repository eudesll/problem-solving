package leet

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func goodNodes(root *TreeNode) int {
	return goodNodesCount(root.Val, root)
}

func goodNodesCount(parent int, node *TreeNode) int {
	if node == nil {
		return 0
	}

	res := goodNodesCount(node.Val, node.Left)
	res += goodNodesCount(node.Val, node.Right)

	if node.Val >= parent {
		res++
	}

	return res
}
