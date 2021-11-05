def is_anagrams(s, t):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    for i in t:
        d[i] = d.get(i, 0) - 1
    for k in d:
        if d[k] !=0:
            return False
    return True


if __name__ == '__main__':
    print(is_anagrams(s='python', t='py'))


