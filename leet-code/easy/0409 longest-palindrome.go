package leet

func longestPalindrome(s string) int {
	lettersCounter := map[rune]int{}
	for _, l := range s {
		lettersCounter[l]++
	}

	possiblePalindrome := 0
	hasOneLetter := false
	for _, qtt := range lettersCounter {
		if qtt%2 != 0 {
			qtt--
			hasOneLetter = true
		}

		if qtt > 1 {
			possiblePalindrome += qtt
		}
	}

	if hasOneLetter {
		possiblePalindrome++
	}

	return possiblePalindrome
}
