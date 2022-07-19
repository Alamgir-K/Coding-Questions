def string_rotation(s1: str, s2: str) -> bool:
    """
    Given two strings, s1 and s2, check if s2 is a rotation of s1

    Time Complexity: O(s1 + s2)
    Space Complexity: O(1)
    """
    if len(s1) != len(s2):
        return False

    return (s2 in (s1 + s1))
    


def test_string_rotation():
    s1 = "waterbottle"
    s2 = "erbottlewat"
    assert string_rotation(s1, s2) == True


if __name__ == "__main__":
    test_string_rotation()
