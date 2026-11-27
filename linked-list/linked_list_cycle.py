def hasCycle(self, head):
    """
    Determines whether a singly linked list contains a cycle,
    using Floyd's tortoise and hare algorithm.

    :param head: The head node of the linked list.
    :return: True if the list has a cycle, otherwise False.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False
