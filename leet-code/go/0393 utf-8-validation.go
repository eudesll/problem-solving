package leet

func validUtf8(data []int) bool {
	mustHave := 0
	for i := 0; i < len(data); i++ {
		if mustHave == 0 {
			mustHave = leftBits(data[i])
			continue
		}

		mustHave -= leftBits(data[i])
	}

	return mustHave == 0
}

func leftBits(n int) int {
	s := 0
	n8 := uint8(n)
	for i := 128; n8&uint8(i) != 0; n8 <<= 1 {
		s++
	}

	return s
}
