import string

from pip import main


def is_unique_dict_implementation(str: string) -> bool:
    """
    Check if a string has all unique characters

    Precondition: str belongs to extended ASCII character set
    """
    if (len(str) > 256):
        return False
    
    char_set = {}

    for char in str:
        if char in char_set:
            return False
        
        char_set[char] = True

    return True

def is_unique_bitwise_implementation(str: string) -> bool:
    """
    Check if a string has all unique characters

    Precondition: str belongs to lowercase letters set
    """
    checker = 0

    for char in str:
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
