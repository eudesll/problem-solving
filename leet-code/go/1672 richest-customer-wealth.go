package leet

func maximumWealth(accounts [][]int) int {
	biggest := -1

	for i := range accounts {
		sum := 0
		for j := range accounts[i] {
			sum += accounts[i][j]
		}

		if sum > biggest {
			biggest = sum
		}
	}

	return biggest
}
