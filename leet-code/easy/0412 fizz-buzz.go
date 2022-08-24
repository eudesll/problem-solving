package leet

import "fmt"

func fizzBuzz(n int) []string {
	ans := make([]string, n)
	for i := 1; i <= n; i++ {
		a := ""

		if i%3 == 0 {
			a += "Fizz"
		}

		if i%5 == 0 {
			a += "Buzz"
		}

		if a == "" {
			a = fmt.Sprint(i)
		}

		ans[i-1] = a
	}

	return ans
}
