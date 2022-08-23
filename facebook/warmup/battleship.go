package warmup

func getHitProbability(R int32, C int32, G [][]int32) float64 {
	totalShips := 0.0
	for _, c := range G {
		for _, v := range c {
			if v == 1 {
				totalShips++
			}
		}
	}

	return totalShips / float64(R*C)
}
