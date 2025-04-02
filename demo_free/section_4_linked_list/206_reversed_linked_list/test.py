class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution:
    def reverse_linked_list(self, head: ListNode):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

if __name__ == "__main__":
    node_3 = ListNode(
        value=3,
        next=None
    )
    node_2 = ListNode(
        value=2,
        next=node_3
    )
    node_1 = ListNode(
        value=1,
        next=node_2
    )
    
    solution = Solution()
    solution.reverse_linked_list(
        head=node_1
    )

    print(node_1.next)
    print(node_2.next.value)
    print(node_3.next.value)
