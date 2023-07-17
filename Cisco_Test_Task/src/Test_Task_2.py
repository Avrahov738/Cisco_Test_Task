# Write a method that answers the following problem: Accept as input:
# · list: an unordered list of arrays each with 4 elements.
# · target: an integer
# Find and display the complete array that contains the provided target number.

def find_array_with_target(unordered_list, target):
    for array in unordered_list:
        if target in array:
            return array
    return None