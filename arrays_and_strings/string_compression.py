def string_compression(s: str) -> str:
    """
    Performs basic string compression using counts of repeated characters

    Example: aabcccccaaa -> a2b1c5a3

    Return compressed string (if shorter). Otherwise return original string

    Time Complexity: O(s1 + s2)
    Space Complexity: O(1)
    """
    compressed = []
    consecutive_count = 0

    for i in range(0, len(s)):
        consecutive_count += 1

        if (i + 1 >= len(s)) or (s[i] != s[i + 1]):
            compressed.append(s[i])
            compressed.append(consecutive_count)
            consecutive_count = 0
    
    if len(compressed) < len(s):
        return "".join(str(e) for e in compressed)
    else:
        return s
    


def test_string_compression():
    s1 = "aabcccccaaa"
    s2 = "abc"
    assert string_compression(s1) == "a2b1c5a3"
    assert string_compression(s2) == "abc"


if __name__ == "__main__":
    test_string_compression()
