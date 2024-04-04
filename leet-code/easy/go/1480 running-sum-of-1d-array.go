package leet

func runningSum(nums []int) []int {
	for i := range nums {
		if i == 0 {
			continue
		}

		nums[i] += nums[i-1]
	}

	return nums
}
