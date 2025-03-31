class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # 暂存下一个节点
            curr.next = prev       # 反转当前指针
            prev = curr            # prev 前进一步
            curr = next_node       # curr 前进一步

        return prev