def two_sum(arr: list) -> int:
    """
    Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.

    Time Complexity: O(n) where n = len(arr) 
    Space Complexity: O(1)
    """
    current = 1
    next = 1

    while current < len(arr):
        if arr[current] != arr[next - 1]:
            arr[next] = arr[current]
            next +=1
        current += 1
    
    return next


def test_two_sum():
    arr1 = [2, 3, 3, 3, 6, 9, 9]
    assert two_sum(arr1) == 4

    arr2 = [2, 2, 2, 11]
    assert two_sum(arr2) == 2


def remove_element_duplicate(arr: list, k: int) -> int:
    """
    Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

    Time Complexity: O(n) where n = len(arr) 
    Space Complexity: O(1)
    """
    next = 0

    for i in range(0, len(arr)):
        if arr[i] != k:
            arr[next] = arr[i]
            next += 1  

    return next

    
def test_remove_element_duplicate():
    arr1 = [3, 2, 3, 6, 3, 10, 9, 3]
    k1 = 3
    assert remove_element_duplicate(arr1, k1) == 4

    arr2 = [2, 11, 2, 2, 1]
    k2 = 2
    assert remove_element_duplicate(arr2, k2) == 2


if __name__ == "__main__":
    test_two_sum()
    test_remove_element_duplicate
