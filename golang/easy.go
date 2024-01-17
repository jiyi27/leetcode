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

// binary search
func searchInsert(nums []int, target int) int {
	l := 0
	r := len(nums) - 1
	for l <= r {
		m := (r + l) / 2
		v := nums[m]
		switch {
		case v < target:
			l = m + 1
		case v > target:
			r = m - 1
		default:
			return m
		}
	}
	return l
}

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	result := &ListNode{}
	current := result

	for list1 != nil && list2 != nil {
		if list1.Val < list2.Val {
			current.Next = list1
			list1 = list1.Next
		} else {
			current.Next = list2
			list2 = list2.Next
		}
		current = current.Next
	}

	if list1 == nil {
		current.Next = list2
	} else {
		current.Next = list1
	}

	return result.Next
}

func climbStairs(n int) int {
	secondLast, last := 0, 1
	for ; n > 0; n-- {
		secondLast, last = last, secondLast+last
	}
	return last
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// binary tree
// https://youtu.be/b_NjndniOqY?si=bgaCMCaqdaqDrmxI
func inorderTraversal(root *TreeNode) []int {
	ans := make([]int, 0)
	var foo func(node *TreeNode)
	foo = func(node *TreeNode) {
		if node == nil {
			return
		}
		foo(node.Left)
		ans = append(ans, node.Val)
		foo(node.Right)
	}
	foo(root)
	return ans
}
