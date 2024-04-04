package leet

func climbStairs(n int) int {
	// steps := map[int]int{}

	// var climbing func(step, n int) int
	// climbing = func(step, n int) int {
	// 	if steps[step] != 0 {
	// 		return steps[step]
	// 	}

	// 	if step > n {
	// 		return 0
	// 	}

	// 	if step == n {
	// 		return 1
	// 	}

	// 	step1 := climbing(step+1, n)
	// 	step2 := climbing(step+2, n)

	// 	steps[step] = step1 + step2
	// 	return steps[step]
	// }

	// return climbing(0, n)
	one := 1
	two := 1

	for i := 0; i < n-1; i++ {
		tmp := one
		one += two
		two = tmp
	}

	return one
}
