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

def delete_duplicates(head):
    #
    """Given a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list.

    Return the linked list sorted as well.

    Input: 1->2->3->3->4->4->5
    Output: 1->2->5

    Input: 1->1
    Output: 1

    Input: 1
    Output: 1

    Intuition for simplest case: if current.next is None, stop
    Intuition for next simplest: if current.next and current.next.next is not
        None, then skip current.next if values are the same
    Since need to make 'jump', need prior value to be kept track
    Always have head as head

    1. Initialize prev as ListNode(None), prev.next as head
    2. While prev.next and prev.next.next, check if val in prev.next
        and prev.next.next is the same.
            If yes, make prev.next = prev.next.next
            If no, pass
    3. Set prev.next to be next value
    """
    prev = ListNode(0)
    prev.next = head

    while prev.next and prev.next.next:
        a = prev.next
        b = prev.next.next
        c = prev.next.next.next  # may be None

        if a.val == b.val:
            prev.next.next = c
        else:
            prev.next.next = b

        prev = prev.next

    return head


if __name__ == "__main__":
    g = ListNode(5)
    f = ListNode(4, g)
    e = ListNode(4, f)
    d = ListNode(3, e)
    c = ListNode(3, d)
    b = ListNode(2, c)
    a = ListNode(1, b)

    print(a)

    result = delete_duplicates(a)
    print(result)
