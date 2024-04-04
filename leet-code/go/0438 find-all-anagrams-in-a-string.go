package leet

func findAnagrams(s string, p string) []int {
	ss := len(s)
	ps := len(p)

	pm := make([]int, 26)
	for _, l := range p {
		pm[l-97]++
	}

	r := []int{}
	for i, l := range s {
		if i+ps > ss {
			break
		}

		if pm[l-97] == 0 {
			continue
		}

		sm := make([]int, 26)
		for _, l := range s[i : i+ps] {
			sm[l-97]++
		}

		if isAnagram(sm, pm) {
			r = append(r, i)
		}
	}

	return r
}

func isAnagram(s, p []int) bool {
	for idx := range p {
		if s[idx] != p[idx] {
			return false
		}
	}

	return true
}

// func findAnagrams(s string, p string) []int {
// 	pm := map[rune]int{}
// 	for _, l := range p {
// 		pm[l]++
// 	}

// 	ss := len(s)
// 	ps := len(p)

// 	r := []int{}
// 	for i := 0; i < ss; i++ {
// 		if s[i] != p[0] {
// 			continue
// 		}

// 		start := i - ps + 1
// 		if start < 0 {
// 			start = 0
// 		}

// 		lo := i
// 		for ; start <= i && start+ps <= ss; start++ {
// 			if !isAnagram(start, ps, s, pm) {
// 				if lo != i {
// 					start = lo
// 				}

// 				continue
// 			}

// 			lo = start + ps - 1
// 			r = append(r, start)
// 		}
// 		i = lo
// 	}

// 	return r
// }

// func isAnagram(start, ps int, s string, pm map[rune]int) bool {
// 	sm := map[rune]int{}
// 	for _, l := range s[start : start+ps] {
// 		sm[l]++
// 	}

// 	for l, q := range sm {
// 		if pm[l] != q {
// 			return false
// 		}
// 	}

// 	return true
// }
