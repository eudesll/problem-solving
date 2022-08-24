package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	tests := [][]int64{
		{3, getMaxAdditionalDinersCount(10, 1, 2, []int64{2, 6})},
		{1, getMaxAdditionalDinersCount(15, 2, 3, []int64{11, 6, 14})},
		{1, getMaxAdditionalDinersCount(10, 1, 4, []int64{1, 3, 6, 10})},
		{2, getMaxAdditionalDinersCount(10, 1, 3, []int64{2, 4, 6})},
		{5, getMaxAdditionalDinersCount(10, 1, 0, []int64{})},
		{4, getMaxAdditionalDinersCount(10, 2, 0, []int64{})},
		{2, getMaxAdditionalDinersCount(10, 3, 1, []int64{5})},
	}

	for _, test := range tests {
		expected := test[0]
		result := test[1]

		if expected != result {
			fmt.Println("Expected: ", expected)
			fmt.Println("Result: ", result)
		}
	}
}

func getMaxAdditionalDinersCount(N int64, K int64, M int32, S []int64) int64 {
	sort.Slice(S, func(i, j int) bool { return S[i] < S[j] })

	free := int64(0)
	seat := int64(1)
	for _, s := range S {
		empty := (s - K) - seat
		free += addDistance(empty, K)
		seat = s + K + 1
	}

	free += addDistance(N+1-seat, K)
	return free
}

func addDistance(free, K int64) int64 {
	if free <= 0 {
		return 0
	}

	calc := float64(free) / (float64(K) + 1.0)
	calc = math.Ceil(calc)
	return int64(calc)
}
