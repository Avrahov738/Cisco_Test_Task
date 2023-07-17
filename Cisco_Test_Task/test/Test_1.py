import sys
sys.path.append('../Cisco_Test_Task/src/')

from Test_Task_1 import LinkedList

# Test Case 1: Empty List
def test_remove_middle_element_empty_list():
    linked_list = LinkedList()
    linked_list.remove_middle_element()
    assert linked_list.head is None

# Test Case 2: List with a Single Node
def test_remove_middle_element_single_node():
    linked_list = LinkedList()
    linked_list.add_element(5)
    linked_list.remove_middle_element()
    assert linked_list.head is None

# Test Case 3: List with Two Nodes
def test_remove_middle_element_two_nodes():
    linked_list = LinkedList()
    linked_list.add_element(10)
    linked_list.add_element(20)

    assert linked_list.head.val == 10
    assert linked_list.head.next.val == 20

    linked_list.remove_middle_element()

    # After removing the middle element, the new head should be the first node (10)
    assert linked_list.head.val == 10
    assert linked_list.head.next is None
# Test Case 4: List with Three Nodes
def test_remove_middle_element_three_nodes():
    linked_list = LinkedList()
    linked_list.add_element(10)
    linked_list.add_element(20)
    linked_list.add_element(30)
    linked_list.remove_middle_element()
    assert linked_list.head.val == 10
    assert linked_list.head.next.val == 30
    assert linked_list.head.next.next is None

# Test Case 5: List with Odd Number of Nodes
def test_remove_middle_element_odd_nodes():
    linked_list = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        linked_list.add_element(value)
    linked_list.remove_middle_element()
    assert linked_list.head.val == 1
    assert linked_list.head.next.val == 2
    assert linked_list.head.next.next.val == 4
    assert linked_list.head.next.next.next.val == 5
    assert linked_list.head.next.next.next.next is None

# Test Case 6: List with Even Number of Nodes
def test_remove_middle_element_even_nodes():
    linked_list = LinkedList()
    for value in [11, 22, 33, 44, 55, 66]:
        linked_list.add_element(value)
    linked_list.remove_middle_element()
    assert linked_list.head.val == 11
    assert linked_list.head.next.val == 22
    assert linked_list.head.next.next.val == 33
    assert linked_list.head.next.next.next.val == 55
    assert linked_list.head.next.next.next.next.val == 66
    assert linked_list.head.next.next.next.next.next is None

# Test Case 7: Edge Case - Middle Element in the First Half
def test_remove_middle_element_middle_first_half():
    linked_list = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        linked_list.add_element(value)
    linked_list.remove_middle_element()
    assert linked_list.head.val == 1
    assert linked_list.head.next.val == 2
    assert linked_list.head.next.next.val == 4
    assert linked_list.head.next.next.next.val == 5
    assert linked_list.head.next.next.next.next is None


# Test Case 8: Edge Case - Middle Element in the Second Half
def test_remove_middle_element_middle_second_half():
    linked_list = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        linked_list.add_element(value)
    linked_list.remove_middle_element()
    assert linked_list.head.val == 1
    assert linked_list.head.next.val == 2
    assert linked_list.head.next.next.val == 4
    assert linked_list.head.next.next.next.val == 5
    assert linked_list.head.next.next.next.next is None

# Test Case 9: Edge Case - Middle Element at the End
def test_remove_middle_element_middle_at_end():
    linked_list = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        linked_list.add_element(value)
    linked_list.remove_middle_element()
    assert linked_list.head.val == 1
    assert linked_list.head.next.val == 2
    assert linked_list.head.next.next.val == 4
    assert linked_list.head.next.next.next.val == 5
    assert linked_list.head.next.next.next.next is None

# Test Case 10: Large List with 100 Elements
def test_remove_middle_element_large_list():
    linked_list = LinkedList()
    for value in range(1, 100):
        linked_list.add_element(value)

    # Removing the middle element (50) from the large list
    linked_list.remove_middle_element()

    # Asserting the head and the first few elements after the removal
    assert linked_list.head.val == 1
    assert linked_list.head.next.val == 2
    assert linked_list.head.next.next.val == 3
    assert linked_list.head.next.next.next.val == 4
   
    # Checking that the middle element (50) is not present in the list anymore
    current = linked_list.head
    while current is not None:
        assert current.val != 50
        current = current.next

    # Asserting that the linked list still has 98 elements
    current = linked_list.head
    count = 0
    while current is not None:
        count += 1
        current = current.next
    assert count == 98

if __name__ == "__main__":
    # Run all the test cases
    test_remove_middle_element_empty_list()
    test_remove_middle_element_single_node()
    test_remove_middle_element_two_nodes()
    test_remove_middle_element_three_nodes()
    test_remove_middle_element_odd_nodes()
    test_remove_middle_element_even_nodes()
    test_remove_middle_element_middle_first_half()
    test_remove_middle_element_middle_second_half()
    test_remove_middle_element_middle_at_end()
    test_remove_middle_element_large_list()

    print("All test cases passed successfully!")