package golang

// IsValid stack
func IsValid(s string) bool {
	// this could be refactored to "if len(s) == 0 || len(s)%2 == 1"
	if len(s) == 0 {
		return true
	}
	if len(s) == 1 {
		return false
	}
	// this could be a map
	var dict = [127]byte{
		'(': ')',
		'[': ']',
		'{': '}',
	}
	stack := make([]rune, 0)
	for _, ch := range s {
		if ch == '{' || ch == '[' || ch == '(' {
			stack = append(stack, ch)
		}
		// key point: when there is a close parentheses,
		// the top on the stack must be the parentheses corresponding to it
		// otherwise this cannot be closed correctly.
		if ch == '}' || ch == ']' || ch == ')' {
			if len(stack) == 0 {
				return false
			}
			if dict[stack[len(stack)-1]] == byte(ch) {
				stack = stack[:len(stack)-1]
				continue
			}
			return false
		}
	}
	return len(stack) == 0
}
