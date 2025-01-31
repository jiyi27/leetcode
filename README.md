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

> `19. removeNthFromEnd` 链表题 也可以使用双指针, 

> 双指针法也并不一定是 刚开始一个快一个慢 也有可能在相同位置, 例如 1047. 删除字符串中的所有相邻重复项, 844. Backspace String Compare
> 这两个题其实是一个题型, 即消除元素后有可能会影响下次的消除, 就像连成一块就可以消掉游戏的那种逻辑, 

### day 3

**题目:** 977. Squares of a Sorted Array

**总结:** 

- 双指针还可以从两端向中间移动, 并不一定是从左到右一个方向
- 左闭右闭时, 要使用 `while left <= right`, 因为 `left == right` 时, 还有一个元素没有处理

**题目:** 209. Minimum Size Subarray Sum

**总结:** 滑动窗口问题也可以看作为双指针

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

### day 3

**总结:** 链表的问题直接画图分析, 单链表的reverse, swap这种一般使用双指针方法, 一个 pre, 一个 curr, 进行一次操作后, 两个指针往后移动.
分析的时候要观察切段的链接, 确保每个节点都是被引用的状态, 否则就会被gc清除了, 因为每个节点本质是个对象而已, 

## 哈希表

### day 1

哈希表就像 map, 有 index, 然后有 index 对应的值, map 的常见实现方法就是 哈希表和红黑树, 前者查询插入都是O(1), 后者是 O(log*n)

使用哈希法来解决问题时, 一般会选择如下三种数据结构:

- array
- set
- map

了解更多: 

- [哈希表理论基础](https://programmercarl.com/%E5%93%88%E5%B8%8C%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)

### day 2

首先我再强调一下什么时候使用哈希法，当我们需要查询一个元素是否出现过，或者一个元素是否在集合里的时候，就要第一时间想到哈希法。

本题呢，我就需要一个集合来存放我们遍历过的元素，然后在遍历数组的时候去询问这个集合，某元素是否遍历过，也就是 是否出现在这个集合。

那么我们就应该想到使用哈希法了。

因为本题，我们不仅要知道元素有没有遍历过，还要知道这个元素对应的下标，需要使用 key value结构来存放，key来存元素，value来存下标，那么使用map正合适。

再来看一下使用数组和set来做哈希法的局限。

- 数组的大小是受限制的，而且如果元素很少，而哈希值太大会造成内存空间的浪费
  - `242. 有效的字母异位词 (opens new window)` 用数组作为哈希表来解决哈希问题
- set是一个集合，里面放的元素只能是一个key，而两数之和这道题目，不仅要判断y是否存在而且还要记录y的下标位置，因为要返回x 和 y的下标。所以set 也不能用。
  - `349. 两个数组的交集 (opens new window)`, 通过set作为哈希表来解决哈希问题

此时就要选择另一种数据结构：map ，map是一种key value的存储结构，可以用key保存数值，用value再保存数值所在的下标。

- [两数之和](https://programmercarl.com/0001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE)

## 字符串

### day 1

字符串处理常见方法双指针, 删除字符串空格 双指针法 即 n^2 -> n

```c
void removeExtraSpaces(string& s) {//去除所有空格并在相邻单词之间添加空格, 快慢指针。
    int slow = 0;   //整体思想参考https://programmercarl.com/0027.移除元素.html
    for (int i = 0; i < s.size(); ++i) { //
        if (s[i] != ' ') { //遇到非空格就处理，即删除所有空格。
            if (slow != 0) s[slow++] = ' '; //手动控制空格，给单词之间添加空格。slow != 0说明不是第一个单词，需要在单词前添加空格。
            while (i < s.size() && s[i] != ' ') { //补上该单词，遇到空格说明单词结束。
                s[slow++] = s[i++];
            }
        }
    }
    s.resize(slow); //slow的大小即为去除多余空格后的大小。
}
```

python 语法, 通过产生新 list 反转字符串:

```python
def reverseWords(s_):
    list_str = s_.split()
    list_str = list_str[::-1]
    return ' '.join(list_str)
```

## 堆栈

### day 1

python 中的 deque 支持下标操作和 popleft 和 pop, append, 因为 queue 是先进先出, 所以使用 `popleft` 是弹出第一个元素, 
`append` 是添加元素, 结构类似 list, 但 pop 操作为 O(1)

list 可以作为栈来用, arr[-1], pop, append()

## 二叉树

### day 1

Recursion 三步走, 确定返回值和参数, 确定终止条件, 确定单层逻辑. 其实**首先要确定的应该是遍历顺序**, 因为遍历顺序决定了递归的顺序, 递归的顺序决定了返回值和参数, 且听我慢慢说来. 

> 使用前序遍历, 需要通过参数(depth + 1)或者全局变量来传递之前函数积攒下来的信息, 比如求最大深度, 第一层数据传给第二层, 依次类推直到最后一层, 后序遍历的逻辑是直接冲到叶子节点, 然后通过返回值层层递加,

使用前序遍历的时候显而易见(函数处理当前节点再进行递归其他字节点 中左右 递归函数的单层逻辑都是处理当前节点), 函数不可以通过返回值来传递信息, 不然后面的单层逻辑没办法处理 (函数直接返回了), 既然无法通过返回值来累积或者传递信息, 我们只能通过一个 state 来传递(记录)每次 recursion 的影响, 所以下面的例子中我们需要全局变量 `self.depth` 和 `self.result`, 

```python
class Solution104:
    def __init__(self):
        self.depth = 0
        self.result = -1

    def maxDepth(self, root):
        def getDepth(node):
            if not node:
                return

            # 前序遍历 中左右
            self.depth += 1
            if self.result < self.depth:
                self.result = self.depth

            if node.left:
                getDepth(node.left)
                self.depth -= 1
            if node.right:
                getDepth(node.right)
                self.depth -= 1

        getDepth(root)
        return self.depth
```

而后序遍历正适合通过返回值的方式来传递信息, 因为当前节点最后处理, 通过下面的例子可以看出:

```python
class Solution104:
    def getDepth(self, node_):
        if not node_:
            return 0
        
        # 后序遍历 左右中
        left_height = self.getDepth(node_.left)
        right_height = self.getDepth(node_.right)
        return 1 + max(left_height, right_height)

    def maxDepth(self, root):
        return self.getDepth(root)
```

> 做二叉树的题要确定遍历顺序, **前序求深度，后序求高度**, 根节点的高度就是二叉树的最大深度, 所以 104.maxDepth 既可以使用前序也可以使用后序.
> 了解更多: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.md


### day 2

每次递归调用都需要单独进行回溯, 回溯即使当前节点恢复到递归之前的状态以便下一个递归的调用 (左节点递归完还需要右节点):

```python
# 二叉树最大深度 递归+回溯
if (node->left) { // 左
    depth++;    // 深度+1
    getdepth(node->left, depth);
    depth--;    // 回溯，深度-1
}
if (node->right) { // 右
    depth++;    // 深度+1
    getdepth(node->right, depth);
    depth--;    // 回溯，深度-1
}
#---------------------#
# 二叉树所有路径 递归+回溯
if node.left:
    self.travel_node(node.left, path, res)
    path.pop()
if node.right:
    self.travel_node(node.right, path, res)
    path.pop()
```

若递归的调用不影响当前节点的状态, 则不用回溯, 上面例子的代码可以简写为:

```python
if (node->left) { // 左
    getdepth(node->left, depth + 1);
}
if (node->right) { // 右
    getdepth(node->right, depth + 1);
}
```

可以发现, 回溯的本质是让之前的函数调用不影响当前节点的状态. 

## 其他

### Bucket Sort

很聪明的方法, 值得深思: [Top K Frequent Elements - Bucket Sort](https://www.youtube.com/watch?v=YPTqKIgVk-k)

## 动态规划 01 背包

```c++
for(int i = 0; i < weight.size(); i++) { // 遍历物品
    for(int j = bagWeight; j >= weight[i]; j--) { // 遍历背包容量
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i]);

    }
}
```