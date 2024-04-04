package leet

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isEvenOddTree(root *TreeNode) bool {
	return checkLevel(root, &[]int{}, 0)
}

// levels hold last value in ordered level nums
func checkLevel(leaf *TreeNode, levels *[]int, deep int) bool {
	if leaf == nil {
		return true
	}

	isFirstInLevel := len(*levels) == deep
	// check 0, 2, ...
	if deep%2 == 0 {
		if leaf.Val%2 != 1 {
			return false
		}
		// is strictly increasing
		if !isFirstInLevel && (*levels)[deep] >= leaf.Val {
			return false
		}
		// check 1, 3, ...
	} else {
		if leaf.Val%2 != 0 {
			return false
		}
		// is strictly decreasing
		if !isFirstInLevel && (*levels)[deep] <= leaf.Val {
			return false
		}
	}
	if isFirstInLevel {
		(*levels) = append(*levels, leaf.Val)
	} else {
		(*levels)[deep] = leaf.Val
	}

	deep++
	if !checkLevel(leaf.Left, levels, deep) {
		return false
	}
	return checkLevel(leaf.Right, levels, deep)
}
