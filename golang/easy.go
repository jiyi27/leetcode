package golang

import (
	"strings"
)

func longestCommonPrefix(s []string) string {
	pref := s[0]
	for i := 1; i < len(s); i++ {
		for !strings.HasPrefix(s[i], pref) {
			pref = pref[:len(pref)-1]
		}
	}
	return pref
}

func isValid(s string) bool {
	if len(s) == 0 || len(s)%2 == 1 {
		return false
	}
	pairs := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}
	stack := make([]rune, 0)
	for _, r := range s {
		if _, ok := pairs[r]; ok {
			stack = append(stack, r)
		} else if len(stack) == 0 || pairs[stack[len(stack)-1]] != r {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}
	return len(stack) == 0
}
