package leet

import (
	"math"
)

func isPowerOfThree(n int) bool {
	if n == 0 {
		return false
	}

	logN := math.Log10(float64(n))
	log3 := math.Log10(3.0)

	check := logN / log3
	checkInt := int(check)
	return check-float64(checkInt) < 0.0000000001
}
