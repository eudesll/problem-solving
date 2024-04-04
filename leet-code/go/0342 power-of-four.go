package leet

import (
	"math"
)

func isPowerOfFour(n int) bool {
	if n == 0 {
		return false
	}

	logN := math.Log(float64(n))
	log4 := math.Log(4.0)

	res := logN / log4
	return res == math.Floor(res)
}
