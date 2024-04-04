package leet

func rotate(matrix [][]int) {
	size := len(matrix)

	nmatrix := make([][]int, size)
	for i := 0; i < size; i++ {
		row := make([]int, size)
		for j := 0; j < size; j++ {
			row[j] = matrix[size-1-j][i]
		}

		nmatrix[i] = row
	}

	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			matrix[i][j] = nmatrix[i][j]
		}
	}
}
