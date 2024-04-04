package leet

func characterReplacement(s string, k int) int {
	r := 0
	idx := 0
	for idx < len(s) {
		nIdx := -1
		letter := s[idx]
		repeats := 1
		replaces := k
		for i := idx + 1; i < len(s); i++ {
			if s[i] != letter {
				if replaces == 0 {
					break
				}

				if nIdx == -1 {
					nIdx = i
				}

				replaces--
			}

			repeats += 1
		}
		repeats += replaces

		if repeats > r {
			r = repeats
		}

		if nIdx == -1 {
			nIdx = idx + repeats
		}

		idx = nIdx
	}

	if r > len(s) {
		r = len(s)
	}

	return r
}
