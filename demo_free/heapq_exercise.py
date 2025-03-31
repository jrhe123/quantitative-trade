import heapq

nums = [5, 1, 3, 8, 2]

# 把列表变成一个堆
heapq.heapify(nums)
print("堆化后的列表:", nums)  # 注意：顺序不是排序，而是堆的结构

# 弹出最小元素
smallest = heapq.heappop(nums)
print("弹出的最小值:", smallest)

# 添加新元素
heapq.heappush(nums, 0)
print("加入 0 后的堆:", nums)

# 弹出并加入（效率更高）
heapq.heappushpop(nums, 4)  # 先加入，再弹出堆顶
print("heappushpop 后的堆:", nums)

# 替换堆顶元素（先 pop 再 push）
heapq.heapreplace(nums, 10)
print("heapreplace 后的堆:", nums)



nums = [5, 1, 3, 8, 2, 7, 4]

# 取最小的 3 个数
smallest_three = heapq.nsmallest(3, nums)
print("最小的三个元素:", smallest_three)

# 取最大的 3 个数
largest_three = heapq.nlargest(3, nums)
print("最大的三个元素:", largest_three)


# 构造最大堆：存放负数
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

# 弹出最大值
max_val = -heapq.heappop(max_heap)
print("最大值:", max_val)

# 添加新元素（-9）
heapq.heappush(max_heap, -9)
print("加入 -9 后的最大堆（负数表示）:", max_heap)





# ===============================合并 K 个有序链表================================================

# 定义链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"{self.val} -> {self.next}"

def mergeKLists(lists):
    heap = []
    
    # 用于区分节点（避免节点值相等时报错）
    count = 0
    
    # 把每个链表的头节点放入堆中
    for l in lists:
        if l:
            heapq.heappush(heap, (l.val, count, l))
            count += 1

    dummy = ListNode()
    current = dummy

    while heap:
        val, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, count, node.next))
            count += 1

    return dummy.next


# 辅助函数：将数组转换为链表
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# 测试
lists = [
    build_list([1, 4, 5]),
    build_list([1, 3, 4]),
    build_list([2, 6])
]

merged = mergeKLists(lists)
print(merged)  # 输出: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6 -> None