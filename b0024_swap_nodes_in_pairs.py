class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        value_array = [self.val]
        next_node = self.next

        while next_node:
            if next_node.val:
                value_array.append(next_node.val)
            else:
                break

            next_node = next_node.next

        return ",".join([str(val) for val in value_array])


def swap_pairs(head: ListNode) -> ListNode:
    """
    Given a linked list, swap every two adjacent nodes and return its head.

    You may not modify the values in the list's nodes. Only nodes itself may be
    changed.

    Input: head = [1,2,3,4]
    Output: [2,1,4,3]
    """
    prev = ListNode(0)
    prev.next = head
    result = prev
    
    while prev.next and prev.next.next:
        a = prev.next
        b = prev.next.next
        c = prev.next.next.next
        prev.next = b
        prev.next.next = a
        prev.next.next.next = c

        prev = prev.next.next

    return result.next


if __name__ == "__main__":
    d = ListNode(4)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(1, b)

    print(a)
    result = swap_pairs(a)
    print(result)
