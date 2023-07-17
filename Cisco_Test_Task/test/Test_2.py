import sys
sys.path.append('../Cisco_Test_Task/src/')
from Test_Task_2 import find_array_with_target

# Test Case 1: Positive Scenario - Target Found in a Single Array
def test_positive_target_in_single_array():
    unordered_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    target = 6
    # Assert that the function correctly returns the array containing the target value
    assert find_array_with_target(unordered_list, target) == [4, 5, 6]

# Test Case 2: Positive Scenario - Target Found in Multiple Arrays (Return First)
def test_positive_target_in_multiple_arrays():
    unordered_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 6, 9, 10]
    ]
    target = 6
    # Assert that the function returns the first array containing the target value
    assert find_array_with_target(unordered_list, target) == [4, 5, 6]

# Test Case 3: Negative Scenario - Target Not Found in Any Array
def test_negative_target_not_found():
    unordered_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    target = 20
    # Assert that the function returns None when the target is not found in any array
    assert find_array_with_target(unordered_list, target) is None

# Test Case 4: Empty List
def test_empty_list():
    unordered_list = []
    target = 5
    # Assert that the function returns None when the list is empty
    assert find_array_with_target(unordered_list, target) is None

# Test Case 5: Large Unordered List - Performance
def test_large_unordered_list_performance():
    unordered_list = [[1, 2, 3, 4] for _ in range(1000)]
    target = 3
    # Assert that the function performs well on a large unordered list
    assert find_array_with_target(unordered_list, target) == [1, 2, 3, 4]

# Test Case 6: Negative Scenario - Target is a List
def test_negative_target_is_list():
    unordered_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9, 10]
    ]
    target = [2, 3]
    # Assert that the function handles invalid targets (lists) and returns None
    assert find_array_with_target(unordered_list, target) is None

# Test Case 7: Arrays with Duplicates - Return First Occurrence
def test_arrays_with_duplicates_return_first_occurrence():
    unordered_list = [
        [1, 2, 3],
        [4, 5, 6, 2, 3],
        [7, 8, 9, 10]
    ]
    target = 3
    # Assert that the function returns the first occurrence of the target value
    assert find_array_with_target(unordered_list, target) == [1, 2, 3]

# Test Case 8: Target Value is Negative
def test_negative_target_value():
    unordered_list = [
        [1, 2, 3],
        [-5, -3, -1],
        [4, 5, 6]
    ]
    target = -3
    # Assert that the function correctly handles negative target values
    assert find_array_with_target(unordered_list, target) == [-5, -3, -1]

# Test Case 9: Arrays with Non-integer Values
def test_arrays_with_non_integer_values():
    unordered_list = [
        [1, 2, 3],
        [4.5, 5, 6],
        [7, 8, 9, 10.5]
    ]
    target = 10.5
    # Assert that the function handles arrays with non-integer values
    assert find_array_with_target(unordered_list, target) == [7, 8, 9, 10.5]

# Test Case 10: Arrays with Different Lengths
def test_arrays_with_different_lengths():
    unordered_list = [
        [1, 2, 3],
        [4, 5],
        [7, 8, 9, 10]
    ]
    target = 5
    # Assert that the function handles arrays with different lengths
    assert find_array_with_target(unordered_list, target) == [4, 5]


# Run all the test functions
if __name__ == "__main__":
    test_positive_target_in_single_array()
    test_positive_target_in_multiple_arrays()
    test_negative_target_not_found()
    test_empty_list()
    test_large_unordered_list_performance()
    test_negative_target_is_list()
    test_arrays_with_duplicates_return_first_occurrence()
    test_negative_target_value()
    test_arrays_with_non_integer_values()
    test_arrays_with_different_lengths()

    print("All test cases passed successfully!")
