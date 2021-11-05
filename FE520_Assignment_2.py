#problem1
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


#problem2
def is_anagrams(s, t):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    for i in t:
        d[i] = d.get(i, 0) - 1
        if d[i] < 0:
            return False
    return True


#problem3
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
    rng = s.split(' ')
    edg = {}
    for i in rng:
        edg[i] = edg.get(i, 0) + 1
    res = []
    for i in range(k):
        max_key = ''
        max_value = 0
        for key in edg:
            value = edg[key]
            if value > max_value:
                max_key = key
                max_value = value
        res.append(max_key)
        edg.pop(max_key)
    return res


#problem4
def mean(con):
    s = 0
    for i in con:
        s += i
    return s / len(con)


def gradient_descent(x, y, epochs, m=0, c=0, L=0.001):
    for t in range(epochs):
        dm, dc = [], []
        for i in range(len(x)):
            xi = x[i]
            yi = y[i]
            yp = xi * m + c
            dm.append(xi * (yp - yi))
            dc.append(yp - yi)
        Dm = mean(dm)
        Dc = mean(dc)
        m = m - L * Dm
        c = c - L * Dc
    return m, c


if __name__ == '__main__':
    print(is_palindrome(121))
    print(is_palindrome(-121))
    print(is_anagrams(s='anagram', t='nagaram'))
    print(top_k_words("i love python, he love coding python; the course is about python.. ", 2))

    m, c, L = 0, 0, 0.001
    x = [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    print(gradient_descent(x, y, 200))
    print(gradient_descent(x, y, 500))
    print(gradient_descent(x, y, 1000))
    print(gradient_descent(x, y, 2000))
    print(gradient_descent(x, y, 3000))

