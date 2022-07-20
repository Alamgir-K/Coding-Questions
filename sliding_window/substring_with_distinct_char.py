def substring_with_distinct_char(s: str, K: int) -> int:
    """
    Given a string, find the length of the longest substring in it with no more than K distinct characters.

    Time Complexity: O(n) where n = len(s)
    Space Complexity: O(1)
    """
    distinct = 0
    window_string = ""
    maximum = 0

    for i in range(0, len(s)):
        if s[i] not in window_string:
            distinct += 1

        window_string += s[i]

        while distinct > K:
            removed = window_string[0]
            window_string = window_string[1:]

            if removed not in window_string:
                distinct -= 1

        maximum = max(maximum, len(window_string))

    return maximum


def test_substring_with_distinct_char():
    s1 = "araaci"
    k = 2
    assert substring_with_distinct_char(s1, k) == 4

    arr2 = "araaci"
    k2 = 3
    assert substring_with_distinct_char(arr2, k2) == 5


if __name__ == "__main__":
    test_substring_with_distinct_char()
