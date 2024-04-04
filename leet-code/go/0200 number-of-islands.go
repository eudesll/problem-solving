package leet

func numIslands(grid [][]byte) int {
	numIslands := 0
	for r := 0; r < len(grid); r++ {
		for c := 0; c < len(grid[r]); c++ {
			if grid[r][c] == '1' {
				removeIsland(grid, r, c)
				numIslands++
			}
		}
	}

	return numIslands
}

func removeIsland(grid [][]byte, r, c int) {
	invalidRow := r < 0 || r >= len(grid)
	invalidColumn := c < 0 || c >= len(grid[0])
	if invalidRow || invalidColumn || grid[r][c] != '1' {
		return
	}

	grid[r][c] = '0'

	removeIsland(grid, r-1, c)
	removeIsland(grid, r+1, c)
	removeIsland(grid, r, c-1)
	removeIsland(grid, r, c+1)
}
