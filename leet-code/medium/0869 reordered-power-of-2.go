package leet

import (
	"fmt"
	"sort"
	"strings"
)

func sortNumber(n int) string {
	sn := fmt.Sprintf("%d", n)
	ss := strings.Split(sn, "")
	sort.Strings(ss)

	return strings.Join(ss, "")
}

func reorderedPowerOf2(n int) bool {
	num := sortNumber(n)
	for i := 0; i < 30; i++ {
		power := sortNumber(1 << i)
		if num == power {
			return true
		}
	}

	return false
}
