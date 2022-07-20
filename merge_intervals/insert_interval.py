def insert_interval(arr: list, new: list) -> list:
    """
    Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    merged = []
    i = 0
    start = 0
    end = 1

    while i < len(arr) and arr[i][end] < new[start]:
        merged.append(arr[i])
        i += 1

    while i < len(arr) and arr[i][start] < new[end]:
        new[start] = min(arr[i][start], new[start])
        new[end] = max(arr[i][end], new[end])
        i += 1

    merged.append(new)

    while i < len(arr):
        merged.append(arr[i])
        i += 1

    return merged


def test_insert_interval():
    print("Intervals after inserting the new interval: " + str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert_interval([[2, 3], [5, 7]], [1, 4])))


if __name__ == "__main__":
    test_insert_interval()
