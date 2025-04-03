from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # 第一步：判断是否有环（快慢指针）
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None  # 无环

        # 第二步：找入环点
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next

        return ptr