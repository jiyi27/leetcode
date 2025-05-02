# LRU缓存（Least Recently Used Cache）是一种缓存淘汰算法, 用于管理有限的缓存空间
# 当缓存满时, LRU会优先移除最近最少使用的数据, 为新数据腾出空间

# 每次访问（读/写）某数据时, 该数据通常被移到队列头部
# 当缓存空间不足时, 移除“最久未使用”的数据（通常是队列尾部）

# 常用哈希表 + 双向链表
# 哈希表：O(1), 快速定位某个 key 是否存在, 以及对应节点的引用
# 双向链表：O(1) 保持节点的访问顺序, 从头到尾依次代表“最近使用”到“最久未使用”

# get(key)：查找键，若存在返回对应值并更新为最近使用；不存在返回-1
# put(key, value)：插入或更新键值对，若缓存满则移除最久未使用项

# 使用场景
# 操作系统页面置换
# 数据库缓冲池
# CDN（内容分发）

# Python 的 OrderedDict 本质上也是 双向链表 + 哈希表 的组合:
# 内部维护一条双向链表, 链表节点按插入顺序或最后访问顺序链接
# 链表节点中存储 key 和 value, 同时哈希表映射 key → 链表节点

from collections import OrderedDict

class LRUCacheWithOrderedDict:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # 如果 key 不存在，返回 -1
        if key not in self.cache:
            return -1
        # 将该 key 提升为最近使用
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # 如果已经存在，先删除旧条目
        if key in self.cache:
            del self.cache[key]
        # 插入新条目（会在末尾）
        self.cache[key] = value
        # 如果超过容量，淘汰最久未使用的（字典头部）
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# 使用示例
if __name__ == "__main__":
    lru = LRUCacheWithOrderedDict(2)
    lru.put(1, 1)      # 缓存 {1:1}
    lru.put(2, 2)      # 缓存 {1:1, 2:2}
    print(lru.get(1))  # 返回 1，缓存 {2:2, 1:1}
    lru.put(3, 3)      # 淘汰 key=2，缓存 {1:1, 3:3}
    print(lru.get(2))  # 返回 -1（未命中）


class LRUCache:
    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 哈希表
        # 伪头部和尾部节点
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """在头部添加节点"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """移除节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        """将节点移到头部"""
        self._remove_node(node)
        self._add_node(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                # 移除最久未使用项
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]
