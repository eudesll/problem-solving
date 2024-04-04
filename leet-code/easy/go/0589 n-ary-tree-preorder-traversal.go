package leet

type Node struct {
	Val      int
	Children []*Node
}

func preorder(root *Node) []int {
	if root == nil {
		return []int{}
	}

	res := []int{root.Val}
	for _, c := range root.Children {
		res = append(res, preorder(c)...)
	}

	return res
}
