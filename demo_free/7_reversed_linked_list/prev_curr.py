class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None      # 初始化前一个节点为空
        curr = head      # 当前节点从 head 开始

        while curr:
            next_node = curr.next  # 暂存当前节点的下一个节点
            curr.next = prev       # 反转当前节点的指针
            prev = curr            # prev 前进一步
            curr = next_node       # curr 前进一步

        return prev  # 此时 prev 指向新链表头
