package leet

func fib(n int) int {
	// if n > 1 {
	// 	return fib(n-1) + fib(n-2)
	// }

	// if n == 1 {
	// 	return 1
	// }

	// return 0
	one := 0
	two := 1

	for i := 0; i < n; i++ {
		tmp := one
		one += two
		two = tmp
	}

	return one
}
