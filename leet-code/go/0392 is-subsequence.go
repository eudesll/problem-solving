package leet

func isSubsequence(s string, t string) bool {
	if len(s) == 0 {
		return true
	}

	j := 0
	for i := range t {
		if t[i] == s[j] {
			j++

			if j == len(s) {
				return true
			}
		}
	}

	return false
}
