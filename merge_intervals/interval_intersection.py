def interval_intersection(a: list, b: list) -> list:
    """
    Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals

    Time Complexity: O(a + b)
    Space Complexity: O(a + b)
    """
    common = []
    i = 0
    j = 0
    start = 0
    end = 1

    while i < len(a) and j < len(b):
        a_overlap_b = a[i][start] >= b[j][start] and a[i][start] <= b[j][end]
        b_overlap_a = b[j][start] >= a[i][start] and b[j][start] <= a[i][end]

        if a_overlap_b or b_overlap_a:
            overlap_start = max(a[i][start], b[j][start])
            overlap_end = min(a[i][end], b[j][end])
            common.append([overlap_start, overlap_end])
        
        if a[i][end] < b[j][end]:
            i += 1
        else:
            j += 1
    
    return common


def test_interval_intersection():
    print("Intervals Intersection: " + str(interval_intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(interval_intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


if __name__ == "__main__":
    test_interval_intersection()
