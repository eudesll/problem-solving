package leet

func numberOfSteps(num int) int {
	i := 0
	for ; num > 0; i++ {
		// if num%2 == 0 {
		// 	num /= 2
		// 	continue
		// }
		if num&1 == 0 {
			num >>= 1
			continue
		}

		num--
	}

	return i
}
