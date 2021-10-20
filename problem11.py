def is_palindrome(s):
    s = str(s)
    return s == s[::-1]


if __name__ == '__main__':
    print(is_palindrome(121))
    print(is_palindrome(-121))