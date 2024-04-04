package leet

import "sort"

func containsDuplicate(nums []int) bool {
	sort.Ints(nums)
	for i := 0; i < len(nums)-1; i++ {
		if nums[i] == nums[i+1] {
			return true
		}
	}

	// exists := map[int]bool{}
	// for _, n := range nums {
	// 	if exists[n] {
	// 		return true
	// 	}

	// 	exists[n] = true
	// }

	return false
}
