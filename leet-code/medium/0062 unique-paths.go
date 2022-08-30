package leet

func uniquePaths(m int, n int) int {
	return binom(m+n-2, min(m-1, n-1))
}

func min(a int, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func binom(n int, k int) int {
	if k == 0 {
		return 1
	}
	return (n - k + 1) * binom(n, k-1) / k
}
