from cmath import inf


def maximum_sum_subarray(arr: list, K: int) -> int:
    """
    Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(1)
    """
    window_sum = 0
    maximum = -inf
    window_start = 0

    for i in range(0, len(arr)):
        window_sum += arr[i]

        if i >= K - 1:
            if window_sum > maximum:
                maximum = window_sum
            window_sum -= arr[window_start]
            window_start += 1

    return maximum


def test_maximum_sum_subarray():
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    assert maximum_sum_subarray(arr, k) == 9

    arr2 = [2, 3, 4, 1, 5]
    k2 = 2
    assert maximum_sum_subarray(arr2, k2) == 7


if __name__ == "__main__":
    test_maximum_sum_subarray()
