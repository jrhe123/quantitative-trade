from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        pA = headA
        pB = headB

        # 两个指针最终会在交点或 None 相遇
        while pA != pB:
            # 到尾后跳到另一条链表头
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA
