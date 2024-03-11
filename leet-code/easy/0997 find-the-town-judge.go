package leet

func findJudge(n int, trust [][]int) int {
	trusts := map[int]bool{}
	trustedBy := map[int]int{}

	if len(trust) == 0 && n == 1 {
		return n
	}

	for _, rel := range trust {
		trusts[rel[0]] = true

		if _, ok := trusts[rel[1]]; !ok {
			trusts[rel[1]] = false
		}

		trustedBy[rel[1]] += 1
	}

	for p, t := range trusts {
		if !t && trustedBy[p] == n-1 {
			return p
		}
	}

	return -1
}
