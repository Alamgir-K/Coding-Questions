def is_unique_dict_implementation(s: str) -> bool:
    """
    Check if a string has all unique characters

    Precondition: s belongs to extended ASCII character set
    """
    if (len(s) > 256):
        return False
    
    char_set = {}

    for char in s:
        if char in char_set:
            return False
        
        char_set[char] = True

    return True

def is_unique_bitwise_implementation(s: str) -> bool:
    """
    Check if a string has all unique characters

    Precondition: s belongs to lowercase letters set
    """
    checker = 0

    for char in s:
        val = ord(char) - ord('a')

        if (checker & (1 << val) > 0):
            return False
        
        checker |= (1 << val)
    
    return True


def test_is_unique():
    fail_str = "alamgir"
    assert is_unique_dict_implementation(fail_str) == False
    assert is_unique_bitwise_implementation(fail_str) == False

    pass_str = "khan"
    assert is_unique_dict_implementation(pass_str) == True
    assert is_unique_bitwise_implementation(pass_str) == True


if __name__ == "__main__":
    test_is_unique()
