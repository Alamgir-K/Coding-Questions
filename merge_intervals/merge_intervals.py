from __future__ import print_function

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge_interval(arr: list) -> list:
    """
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    arr.sort(key=lambda x:x.start)
    merged = []
    start = arr[0].start
    end = arr[0].end

    for i in range(1, len(arr)):
        interval = arr[i]

        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged.append(Interval(start, end))
    return merged


def any_merge_interval(arr: list) -> bool:
    """
    Given a set of intervals, find out if any two intervals overlap.

    Time Complexity: O(nlogn)
    Space Complexity: O(n)
    """
    arr.sort(key=lambda x:x.start)
    start = arr[0].start
    end = arr[0].end

    for i in range(1, len(arr)):
        interval = arr[i]

        if interval.start <= end:
            return True
        else:
            start = interval.start
            end = interval.end

    return False
    


def test_merge_interval():
    print("Merged intervals: ", end='')
    for i in merge_interval([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()
    assert any_merge_interval([Interval(1, 4), Interval(2, 5), Interval(7, 9)]) == True

    print("Merged intervals: ", end='')
    for i in merge_interval([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()
    assert any_merge_interval([Interval(2, 4), Interval(5, 9)]) == False

    print("Merged intervals: ", end='')
    for i in merge_interval([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()
    assert any_merge_interval([Interval(1, 4), Interval(2, 6), Interval(3, 5)]) == True


if __name__ == "__main__":
    test_merge_interval()
