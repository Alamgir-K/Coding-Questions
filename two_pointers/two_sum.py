def two_sum(arr: str, target: int) -> int:
    """
    Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
    Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

    Time Complexity: O(n) where n = len(arr) 
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        
        if current_sum > target:
            right -= 1
        else:
            left += 1
    
    return [-1, -1]


def test_two_sum():
    arr1 = [1, 2, 3, 4, 6]
    t1 = 6
    assert two_sum(arr1, t1) == [1, 3]

    arr2 = [2, 5, 9, 11]
    t2 = 11
    assert two_sum(arr2, t2) == [0, 2]


if __name__ == "__main__":
    test_two_sum()
