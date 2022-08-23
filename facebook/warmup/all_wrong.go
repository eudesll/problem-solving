package warmup

func getWrongAnswers(N int32, C string) string {
	answers := map[rune]rune{
		'A': 'B',
		'B': 'A',
	}

	r := []rune(C)
	for i, v := range r {
		r[i] = answers[v]
	}

	return string(r)
}
