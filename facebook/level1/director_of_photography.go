package main

import "math"

func getArtisticPhotographCount(N int32, C string, X int32, Y int32) int32 {
	positions := map[rune][]float64{
		'P': {},
		'A': {},
		'B': {},
	}
	for i, c := range C {
		if c == '.' {
			continue
		}

		positions[c] = append(positions[c], float64(i))
	}

	validPositions := int32(0)
	for _, a := range positions['A'] {
		for _, p := range positions['P'] {
			dAP := int32(math.Abs(a - p))
			if dAP < X || dAP > Y {
				continue
			}
      
			for _, b := range positions['B'] {
				dAB := int32(math.Abs(a - b))
				if a < p && a < b || a > p && a > b || dAB < X || dAB > Y {
					continue
				}
        
				validPositions++
			}
		}
	}

	return validPositions
}
