def triplet_sum_to_zero(arr: list) -> list:
    """
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

    Time Complexity: O(nlogn + n^2) where n = len(arr)
    Space Complexity: O(n)
    """
    def search_pair(arr, target, left, triplets):
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                triplets.append([-target, arr[left], arr[right]])
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            
            elif target > current_sum:
                left += 1
            else:
                right -= 1


    triplets = []
    arr.sort()

    for i in range(0, len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)
    
    return triplets
    

def test_triplet_sum_to_zero():
    arr = [-3, 0, 1, 2, -1, 1, -2]
    assert triplet_sum_to_zero(arr) == [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]

    arr2 = [-5, 2, -1, -2, 3]
    assert triplet_sum_to_zero(arr2) == [[-5, 2, 3], [-2, -1, 3]]


if __name__ == "__main__":
    test_triplet_sum_to_zero()
