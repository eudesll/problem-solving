package leet

func topKFrequent(nums []int, k int) []int {
	counter := map[int]int{}
	for _, n := range nums {
		counter[n]++
	}

	// O(KlogN)
	allFrequencies := make([][]int, len(nums))
	for n, f := range counter {
		nf := allFrequencies[f-1]
		if nf == nil {
			nf = []int{}
		}

		allFrequencies[f-1] = append(nf, n)
	}

	rank := []int{}
	for i := len(nums) - 1; k > 0; i-- {
		nf := allFrequencies[i]
		if nf == nil {
			continue
		}

		smallest := len(nf)
		if k < smallest {
			smallest = k
		}

		rank = append(rank, nf[0:smallest]...)
		k -= smallest
	}

	// O(NlogN)
	// rank := make([]int, len(counter))
	// i := 0
	// for n := range counter {
	// 	rank[i] = n
	// 	i++
	// }
	// sort.Slice(rank, func(i, j int) bool {
	// 	return counter[rank[i]] > counter[rank[j]]
	// })
	// rank = rank[0:k]

	return rank
}
