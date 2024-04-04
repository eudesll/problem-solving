package leet

func isIsomorphic(s string, t string) bool {
	mapS := map[byte]byte{}
	mapT := map[byte]byte{}

	for i := range s {
		vs := s[i]
		vt := t[i]

		if mapS[vs] != byte(0) && mapS[vs] != vt ||
			mapT[vt] != byte(0) && mapT[vt] != vs {
			return false
		}

		mapS[vs] = vt
		mapT[vt] = vs
	}

	return true
}
