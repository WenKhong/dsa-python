def reverseList(self, head):
    """
    Reverses a singly linked list.

    :param head: The head node of the linked list.
    :return: The new head node of the reversed linked list.
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev