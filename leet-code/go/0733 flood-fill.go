package leet

import "fmt"

func floodFill(image [][]int, sr int, sc int, color int) [][]int {
	sourceColor := image[sr][sc]
	alreadyChanged := map[string]bool{}

	var fillColor func(sr int, sc int)
	fillColor = func(sr int, sc int) {
		hash := fmt.Sprintf("%d_%d", sr, sc)
		invalidRow := sr < 0 || sr >= len(image)
		invalidColumn := sc < 0 || sc >= len(image[0])
		if invalidRow || invalidColumn ||
			image[sr][sc] != sourceColor ||
			alreadyChanged[hash] {
			return
		}

		alreadyChanged[hash] = true

		fillColor(sr-1, sc)
		fillColor(sr+1, sc)
		fillColor(sr, sc-1)
		fillColor(sr, sc+1)

		image[sr][sc] = color
	}
	fillColor(sr, sc)

	return image
}
