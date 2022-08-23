package leet

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) [][]int {
	if root == nil {
		return nil
	}

	level := [][]int{{root.Val}}

	l := levelOrder(root.Left)
	r := levelOrder(root.Right)
	ls := len(l)
	lr := len(r)

	for i := 0; i < ls || i < lr; i++ {
		childs := []int{}
		if i < ls {
			childs = l[i]
		}

		if i < lr {
			childs = append(childs, r[i]...)
		}

		level = append(level, childs)
	}

	return level
}
