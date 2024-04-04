package leet

func twoSum(nums []int, target int) []int {
	numsM := map[int]int{}
	out := make([]int, 2)

	for i, num := range nums {
		if ix, ok := numsM[target-num]; ok {
			return []int{ix, i}
		}

		numsM[num] = i
	}

	return out
}
