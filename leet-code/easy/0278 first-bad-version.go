package leet

func isBadVersion(version int) bool

func firstBadVersion(n int) int {
	return binarySearch1(1, n)
}

func binarySearch1(start, end int) int {
	length := end - start
	pos := (length / 2) + start

	if length == 0 {
		return pos
	}

	if isBadVersion(pos) {
		return binarySearch1(start, pos)
	}

	return binarySearch1(pos+1, end)
}
