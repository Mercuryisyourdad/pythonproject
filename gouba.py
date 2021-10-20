def is_anagrams(s, t):
    d = {}
    f = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    for z in t:
        f[z] = f.get(z, 0) + 1
    for key in d:
        if (key not in f):
            return False
        if d[key] != f[key]:
            return False
    return True


if __name__ == '__main__':
    print(is_anagrams(s='anagram', t='nagaram'))