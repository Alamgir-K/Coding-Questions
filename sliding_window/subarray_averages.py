def subarray_average(arr: list, K: int) -> list:
    """
    Given an array, find the average of all subarrays of K contiguous elements in it.

    Time Complexity: O(n) where n = len(arr)
    Space Complexity: O(1)
    """
    window_start, window_sum = 0, 0
    result = []

    for i in range(0, len(arr)):
        window_sum += arr[i]

        if i >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1

    return result
    

def test_subarray_average():
    arr = [1, 3, 2, 6, -1, 4, 1]
    k = 5
    assert subarray_average(arr, k) == [2.2, 2.8, 2.4]


if __name__ == "__main__":
    test_subarray_average()
