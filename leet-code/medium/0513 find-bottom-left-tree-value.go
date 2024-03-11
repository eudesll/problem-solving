package leet

import "container/list"

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findBottomLeftValue(root *TreeNode) int {
	result := root.Val
	queue := list.New()
	queue.PushBack(root)

	for queue.Len() > 0 {
		current := queue.Front().Value.(*TreeNode)
		queue.Remove(queue.Front())

		result = current.Val

		if current.Right != nil {
			queue.PushBack(current.Right)
		}
		if current.Left != nil {
			queue.PushBack(current.Left)
		}
	}

	return result
}
