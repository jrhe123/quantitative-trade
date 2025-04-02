class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def merge_two_sort_list(self, l1: ListNode, l2: ListNode):
        if not l1 or not l2:
            return l1 or l2
        
        if l1.value < l2.value:
            l1.next = self.merge_two_sort_list(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_sort_list(l1, l2.next)
            return l2

if __name__ == "__main__":
    pass