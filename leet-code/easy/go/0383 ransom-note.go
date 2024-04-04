package leet

func canConstruct(ransomNote string, magazine string) bool {
	magazineLetters := map[rune]int{}
	noteLetters := map[rune]int{}

	for _, l := range magazine {
		magazineLetters[l]++
	}

	for _, l := range ransomNote {
		noteLetters[l]++
	}

	for l, q := range noteLetters {
		if magazineLetters[l] < q {
			return false
		}
	}

	return true
}
