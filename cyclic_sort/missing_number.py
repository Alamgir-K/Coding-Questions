def missing_number(arr: list) -> list:
    """
    We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
    Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

    Time Complexity: O(n) where n = len(arr) 
    Space Complexity: O(1)
    """
    i = 0
    n = len(arr)

    while i < n:
        j = arr[i]

        if arr[i] < n and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    
    for i in range(0, len(arr)):
        if arr[i] != i:
            return i
    
    return -1
    
    
def test_missing_number():
    print(missing_number([4, 0, 3, 1]))
    print(missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


if __name__ == "__main__":
        test_missing_number()
