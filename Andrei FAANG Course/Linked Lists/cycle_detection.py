def detect_cycle(head):
    # Initialize slow and fast pointers
    slow = head
    fast = head
    while True:
        if not head: return None

        if not head.next: return None

        slow = head
        fast = head
        while True:
            # check for linearity in list
            slow = slow.next
            fast = fast.next
            if fast is None or fast.next is None:
                return None
            else:
                fast = fast.next

            if slow == fast:
                meetNode = slow
                break

        while head != meetNode:
            head = head.next
            meetNode = meetNode.next

        return head
