def one_away(s1: str, s2: str) -> bool:
    """
    Check if two strings are one edit away (insert, delete or replace)

    Time Complexity: O(s1 + s2)
    Space Complexity: O(1)
    """
    if abs(len(s1) - len(s2)) > 1:
        return False

    small_index = 0
    bigger_index = 0
    edit_flag = False

    if len(s1) < len(s2):
        smaller = s1
        bigger = s2
    else:
        smaller = s2
        bigger = s1

    while (small_index < len(smaller) and bigger_index < len(bigger)):
        if smaller[small_index] != bigger[bigger_index]:
            if edit_flag:
                return False
            else:
                edit_flag = True
            
            if len(smaller) == len(bigger):
                small_index += 1
        else:
            small_index += 1

        bigger_index += 1
    
    return True


def test_one_away():
    s1 = "mail"
    s2 = "hail"
    s3 = "bale"
    assert one_away(s1, s2) == True
    assert one_away(s1, s3) == False


if __name__ == "__main__":
    test_one_away()
