package leet

import "fmt"

func groupAnagrams(strs []string) [][]string {
	groups := map[string][]string{}
	for _, str := range strs {
		letters := map[rune]int{}
		for _, l := range str {
			letters[l]++
		}

		hash := fmt.Sprintf("%v", letters)

		group := groups[hash]
		if group == nil {
			group = []string{}
		}

		groups[hash] = append(group, str)
	}

	res := [][]string{}
	for _, a := range groups {
		res = append(res, a)
	}

	return res
}
