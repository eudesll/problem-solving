package leet

import "math"

func maxProfit(prices []int) int {
	lowestPrice := math.MaxInt
	profit := 0

	for _, price := range prices {
		if price < lowestPrice {
			lowestPrice = price
		}

		if price-lowestPrice > profit {
			profit = price - lowestPrice
		}
	}

	return profit
}
