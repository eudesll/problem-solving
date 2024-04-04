package leet

import "math"

func romanToInt(s string) int {
	romanValues := map[byte]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

	total := 0
	prev := math.MinInt
	for i := len(s) - 1; i >= 0; i-- {
		val := romanValues[s[i]]

		if val < prev {
			total -= val
		} else {
			total += val
		}

		prev = val
	}

	return total
}
