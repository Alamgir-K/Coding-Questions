def happy_number(num: int) -> int:
    """
    Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. 
    Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
    """
    def sqaure(num):
        sum = 0

        while num > 0:
            sum += (num % 10) ** 2
            num = num // 10
        
        return sum

    slow = num
    fast = num

    while fast != 1 and sqaure(fast) != 1:
        slow = sqaure(slow)
        fast = sqaure(sqaure(fast))

        if slow == fast:
            return False

    
    return True
    


def test_happy_number():
    assert happy_number(23) == True
    assert happy_number(12) == False


if __name__ == "__main__":
    test_happy_number()
