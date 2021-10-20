def is_palindrome(s):
    s = str(s)
    a = 0
    b = len(s) - 1
    while a <= b:
        if s[a] != s[b]:
            return False
        a += 1
        b -= 1
    return True


if __name__ == '__main__':
    print(is_palindrome(121))
    print(is_palindrome(-121))
