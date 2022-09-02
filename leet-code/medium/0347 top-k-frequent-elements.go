package leet

import "sort"

func topKFrequent(nums []int, k int) []int {
	counter := map[int]int{}
	for _, n := range nums {
		counter[n]++
	}

	rank := make([]int, len(counter))
	i := 0
	for n := range counter {
		rank[i] = n
		i++
	}

	sort.Slice(rank, func(i, j int) bool {
		return counter[rank[i]] > counter[rank[j]]
	})

	return rank[0:k]
}
