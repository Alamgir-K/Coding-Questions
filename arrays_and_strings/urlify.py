def urlify_v1(s: str, n: int) -> str:
    """
    Replace all spaces in a str with '%20'

    Precondition: - s has sufficient space at the end for additional characters
                  - n is the true length of the string

    """
    space_counter = 0

    for i in range(0, n):
        if s[i] == ' ':
            space_counter += 1
        
    index = n + (space_counter * 2)
    str_list = list(s)

    for j in range(n - 1, -1, -1):
        if s[j] == ' ':
            str_list[index - 1] = '0'
            str_list[index - 2] = '2'
            str_list[index - 3] = '%'
            index -= 3
        else:
            str_list[index - 1] = s[j]
            index -= 1
    
    url_string = ""

    for char in str_list:
        url_string += char

    return url_string

def urlify_v2(s: str, n: int) -> str:
    """
    Replace all spaces in a str with '%20'

    Precondition: - s has sufficient space at the end for additional characters
                  - n is the true length of the string

    """
    str_list = s.split()

    url_string = ""

    for i in range(0, len(str_list) - 1):
        url_string = url_string + str_list[i] + "%20"
    
    url_string += str_list[-1]

    return url_string


def test_urlify():
    s = "Mr John Smith    "
    n = 13
    actual = urlify_v1(s, n)
    expected = "Mr%20John%20Smith"
    assert actual == expected

    actual_v2 = urlify_v2(s, n)
    assert actual_v2 == expected

if __name__ == "__main__":
    test_urlify()
