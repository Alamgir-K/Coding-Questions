import math

def maximum_sum_subarray(arr: list, K: int) -> int:
    """
    Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(1)
    """

    window_start = 0
    window_sum = 0
    minimum = math.inf

    for i in range(0, len(arr)):
        window_sum += arr[i]

        while window_sum >= K:
            minimum = min(minimum, ((i - window_start) + 1))
            window_sum -= arr[window_start]
            window_start += 1
    
    if minimum != math.inf:
        return minimum
    else:
        return 0
    


def test_maximum_sum_subarray():
    arr = [2, 1, 5, 2, 3, 2]
    k = 7
    assert maximum_sum_subarray(arr, k) == 2

    arr2 = [2, 1, 5, 2, 8]
    k2 = 7
    assert maximum_sum_subarray(arr2, k2) == 1


if __name__ == "__main__":
    test_maximum_sum_subarray()
