def count(s):
    d = {}
    for i in list(s):
        d[i] = d.get(i, 0) + 1
    return d


z = [1, 2, 3, 4, 5, 2, 1, 7]
print(count(z))



string='   This string is for TEST.    '
print (string.strip() )            # remove both leading and trailing spaces