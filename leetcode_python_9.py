"""
9. Palindrome Number
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

def isPalindrome(x: int) -> bool:
    # solve by converting to string
    # str_x = str(x)
    # rev_str_x = str_x[::-1]
    # return str_x == rev_str_x

    # solve without converting to string
    if x<0 or (x!=0 and x%10==0): return False
    res = 0
    while x>res:
        res = res*10 + x%10
        x = x//10
    
    return x==res or x == res//10

if __name__ == "__main__":
    test_cases = [121, -121, 10]
    test_results = [True, False, False]
    for i in range(len(test_cases)):
        response = isPalindrome(test_cases[i])
        assert test_results[i] == response