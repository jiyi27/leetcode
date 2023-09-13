package done_by_myself

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

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	if list1 == nil && list2 == nil {
		return nil
	}
	res := &ListNode{}
	tem := res
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			tem.Val = list1.Val
			list1 = list1.Next
		} else {
			tem.Val = list2.Val
			list2 = list2.Next
		}
		tem.Next = &ListNode{}
		tem = tem.Next
	}

	for list1 != nil {
		tem.Val = list1.Val
		list1 = list1.Next
		if list1 != nil {
			tem.Next = &ListNode{}
			tem = tem.Next
		}
	}
	for list2 != nil {
		tem.Val = list2.Val
		list2 = list2.Next
		if list2 != nil {
			tem.Next = &ListNode{}
			tem = tem.Next
		}
	}
	return res
}
