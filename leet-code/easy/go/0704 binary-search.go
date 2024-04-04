package leet

func search(nums []int, target int) int {
	return binarySearch(nums, 0, len(nums), target)
}

func binarySearch(nums []int, start, end, target int) int {
	length := end - start
	if length%2 == 0 {
		length--
	}

	pos := (length / 2) + start
	if nums[pos] == target {
		return pos
	}

	if len(nums[start:end]) == 1 {
		return -1
	}

	if nums[pos] > target {
		return binarySearch(nums, start, pos, target)
	}

	return binarySearch(nums, pos+1, end, target)
}
