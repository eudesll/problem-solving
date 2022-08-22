package leet

func isBadVersion(version int) bool

func firstBadVersion(n int) int {
	return binarySearch(1, n)
}

func binarySearch(start, end int) int {
	length := end - start
	pos := (length / 2) + start

	if length == 0 {
		return pos
	}

	if isBadVersion(pos) {
		return binarySearch(start, pos)
	}

	return binarySearch(pos+1, end)
}
