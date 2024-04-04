package leet

import (
	"sort"
	"strings"
)

func sortString(s string) string {
	ss := strings.Split(s, "")
	sort.Strings(ss)

	return strings.Join(ss, "")
}

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	// O(NlogN) - O(1)
	s = sortString(s)
	t = sortString(t)

	for i := range s {
		if s[i] != t[i] {
			return false
		}
	}

	// O(N) - O(N)
	// letters := map[byte]int{}
	// for i := range s {
	// 	letters[s[i]]++
	// 	letters[t[i]]--
	// }

	// for _, q := range letters {
	// 	if q != 0 {
	// 		return false
	// 	}
	// }

	return true
}
