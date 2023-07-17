# Write a method that answers the following problem: Accept as input:
# · list: a singly-linked list
# Remove the middle element of the list without iterating the list more than once. Assume the list size cannot be known until traversed.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = ListNode(value)

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next

    def remove_middle_element(self):
        if self.head is None:
            return 

        slow = self.head
        fast = self.head
        prev = None

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if prev is None:
            self.head = slow.next
        else:
            prev.next = slow.next

    def print_linked_list(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.val))
            current = current.next
        print(" -> ".join(elements))