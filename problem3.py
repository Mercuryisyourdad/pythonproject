def top_k_words(s, k):
    def clean_punctuation(s):
        d = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1,
             'h': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1,
             'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
             'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1, ' ': 1}
        s = s.strip()
        z = ""
        for i in s:
            if i in d:
                z += i
        return z

    s = clean_punctuation(s)
    li = s.split(' ')
    rng = []
    for i in li:
        if i !="":
            rng.append(i)
    edg = {}
    for i in rng:
        edg[i] = edg.get(i, 0) + 1
    res = []
    for i in range(k):
        max_key = ''
        max_value = -1
        for key in edg:
            value = edg[key]
            if value > max_value:
                max_key = key
                max_value = value
        res.append(max_key)
        edg.pop(max_key)
    return res


if __name__ == '__main__':
    print(top_k_words("   i love python, he    love coding python. the course is about python. ", 2))
