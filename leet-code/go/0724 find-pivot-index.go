package leet

import "fmt"

func pivotIndex(nums []int) int {
	sums := map[string]int{}
	prevSum := 0
	for i := len(nums) - 1; i >= 0; i-- {
		sum := nums[i] + prevSum
		prevSum = sum

		sums[hash(sum, i)] = i
	}
	sums[hash(0, len(nums))] = len(nums)

	sum := 0
	for i, v := range nums {
		idx := hash(sum, i+1)
		if sums[idx] == i+1 {
			return sums[idx] - 1
		}

		sum += v
	}

	return -1
}

func hash(val, idx int) string {
	return fmt.Sprintf("%d_%d", val, idx)
}
