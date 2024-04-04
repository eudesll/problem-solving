package leet

func firstUniqChar(s string) int {
	letterQtt := map[rune]int{}

	for _, l := range s {
		letterQtt[l] += 1
	}

	for i, l := range s {
		if letterQtt[l] == 1 {
			return i
		}
	}

	return -1
}
