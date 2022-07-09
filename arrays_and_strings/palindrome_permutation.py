def palindrome_permutation_dict_implementation(s: str,) -> bool:
    """
    Check if the given string is a permutation of a palindrome

    Time Complexity: O(s)
    Space Complexity: O(s)
    """
    odd_count = 0
    char_dict = {}

    for char in s:
        if char != " ":
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

            if char_dict[char] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
    
    return odd_count <= 1


def palindrome_permutation_bitwise_implementation(s: str,) -> bool:
    """
    Check if the given string is a permutation of a palindrome

    Time Complexity: O(s)
    Space Complexity: O(1)
    """
    def create_bit_vector(s):
        vector = 0
        for char in s:
            if char != " ":
                vector = toggle_bit(vector, ord(char))
        return vector

    def toggle_bit(vector, index):
        if index < 0:
            return vector
        
        mask = 1 << index
        if (vector & mask) == 0:
            vector |= mask
        else:
            vector &= ~mask
        
        return vector
    
    vector = create_bit_vector(s)
    return (vector == 0) or (vector & (vector - 1) == 0)


def test_palindrome_permutation():
    s1 = "tact coa"
    assert palindrome_permutation_dict_implementation(s1) == True
    assert palindrome_permutation_bitwise_implementation(s1) == True

    s2 = "hello"
    assert palindrome_permutation_dict_implementation(s2) == False
    assert palindrome_permutation_bitwise_implementation(s2) == False


if __name__ == "__main__":
    test_palindrome_permutation()
