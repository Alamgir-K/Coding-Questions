from collections import Counter

def is_permutation(s1: str, s2: str) -> bool:
    """
    Check if two strings are permutations of one another

    Precondition: both strings belong to extended ASCII character set
    """
    if len(s1) != len(s2):
        return False
    
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)

    return s1_counter == s2_counter



def test_is_permutation():
    s1 = "alamgir"
    s2 = "rigmala"
    assert is_permutation(s1, s2) == True

    s3 = "hello"
    s4 = "hi"
    assert is_permutation(s3, s4) == False

if __name__ == "__main__":
    test_is_permutation()
