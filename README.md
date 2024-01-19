## day 1

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

2. 左闭右开的区间里 `[left, right)`

```python
    lo = 0
    hi = len(nums)  # [left, right)
    while lo < hi:  # 要使用 <, 因为left == right是没有意义的
        ...
```

> `if (nums[middle] > target)` `right` 更新为 `middle`, 而不是 `middle-1`, 因为当前 `nums[middle]` 不等于target, 去左区间继续寻找, 而寻找区间是左闭右开区间, 所以right更新为middle

参考: [代码随想录](https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E6%80%9D%E8%B7%AF)