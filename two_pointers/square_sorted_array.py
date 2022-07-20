def square_sorted_array(arr: list) -> list:
    """
    Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

    Time Complexity: O(n) where n = len(arr) 
    Space Complexity: O(1)
    """
    squares = [0] * len(arr)
    left = 0
    right = len(arr) - 1
    highest = len(arr) - 1

    while left <= right:
        left_sqaure = arr[left] ** 2
        right_square = arr[right] ** 2

        if left_sqaure > right_square:
            squares[highest] = left_sqaure
            left += 1
        else:
            squares[highest] = right_square
            right -= 1
        
        highest -= 1
    
    return squares


def test_square_sorted_array():
    arr1 = [-2, -1, 0, 2, 3]
    assert square_sorted_array(arr1) == [0, 1, 4, 4, 9]

    arr2 = [-3, -1, 0, 1, 2]
    assert square_sorted_array(arr2) == [0, 1, 1, 4, 9]


if __name__ == "__main__":
    test_square_sorted_array()
