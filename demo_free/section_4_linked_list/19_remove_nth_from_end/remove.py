from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 虚拟头节点，简化删除头节点的情况
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # fast 先走 n+1 步，确保 slow 指向待删除节点的前一个
        for _ in range(n + 1):
            fast = fast.next

        # fast 和 slow 一起走，直到 fast 到尾部
        while fast:
            fast = fast.next
            slow = slow.next

        # 删除节点
        slow.next = slow.next.next

        return dummy.next
