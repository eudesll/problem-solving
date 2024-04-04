package leet

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func averageOfLevels(root *TreeNode) []float64 {
	levels := map[int]float64{}
	qtt := map[int]float64{}
	bLevel := 0

	var checkLevel func(level int, node *TreeNode)
	checkLevel = func(level int, node *TreeNode) {
		if node == nil {
			return
		}

		levels[level] += float64(node.Val)
		qtt[level]++

		checkLevel(level+1, node.Left)
		checkLevel(level+1, node.Right)

		if level > bLevel {
			bLevel = level
		}
	}

	checkLevel(0, root)

	res := make([]float64, bLevel)
	for i := range res {
		res[i] = levels[i] / qtt[i]
	}

	return res
}
