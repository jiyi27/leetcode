## 数组

### day 1

对数组循环边界的处理, 如何确定循环不变量, 要根据不同的情况分析

**题目:** Search Insert Position, Binary Search

**总结:**

1. 左闭右闭的区间 `[left, right]`:

```python
lo = 0
hi = len(nums) - 1  # [left, right]
while lo <= hi:  # 要使用 <=, 因为left == right是有意义的
    ...
```

> `if (nums[middle] > target)`, `right` 更新为 `middle - 1`, 因为当前 `nums[middle]` 不等于target, 去左区间继续寻找, 而寻找区间是左闭右闭区间

2. 左闭右开的区间里 `[left, right)`

```python
    lo = 0
    hi = len(nums)  # [left, right)
    while lo < hi:  # 要使用 <, 因为left == right是没有意义的
        ...
```

> `if (nums[middle] > target)`, `right` 更新为 `middle`, 而不是 `middle-1`, 因为当前 `nums[middle]` 不等于target, 去左区间继续寻找, 而寻找区间是左闭右开区间, 所以 `right` 更新为 `middle`

参考: [代码随想录](https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E6%80%9D%E8%B7%AF)

### day 2

双指针 快慢指针法

- 快指针：指向最新的元素, 每次都会移动
- 慢指针：指向 “新数组” 下标的最后位置, 根据条件移动

**题目:** 27. Remove Element, 283. Move Zeroes, 844. Backspace String Compare

**总结:** 数组的元素在内存地址中是连续的, 不能单独删除数组中的某个元素, 只能覆盖, 如果非要删除, 则需要遍历后面的每个元素移动到前面, 

> Python 中字符串是不可变的, 不可按下标操作修改, 可通过 `list(s)` 转换为列表, 然后操作列表, 最后通过 `"".join(list)` 转换为字符串

### day 3

**题目:** 977. Squares of a Sorted Array

**总结:** 

- 双指针还可以从两端向中间移动, 并不一定是从左到右一个方向
- 左闭右闭时, 要使用 `while left <= right`, 因为 `left == right` 时, 还有一个元素没有处理

**题目:** 209. Minimum Size Subarray Sum

**总结:**

- 滑动窗口问题也可以看作为双指针

## 链表

### day 1

**题目:** 203. Remove Linked List Elements

**总结:** 若有需要删除节点的需求, 可以增个 dummy_head, 以便统一化移除头部元素和其他元素:

```python
cur = dummy_head = ListNode(next_=head)
```
### day 2

**题目:** 707. Design Linked List

**总结:** 链表增删改查, 基本操作, 主要是边界条件的处理, 这个可以借助循环不变量的概念, 如删除第 `index` 个元素:

```python
def deleteAtIndex(self, index):
    if index >= self.size or index < 0:
        return

    temp = self.dummy_head
    while index > 0:
        temp, index = temp.next, index - 1
    temp.next = temp.next.next
    self.size -= 1
```

`while index > 0` 可以先写成 `while index >= 0`, 等里面的逻辑写完在考虑边界问题, 只需要考虑边界条件,
比如 `index == 0` 时, 你想不想让循环执行, 然后再考虑 `index=1` 时 (普通情况), 若程序符合预期, 则之后的 `index=2,3,4...` 也肯定符合预期.
