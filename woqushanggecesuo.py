def divison(gou, ba):
    a = gou / ba
    s = '%0.3f' % a
    return s


print(divison(3, 5))


def count(s):
    a = s.split(' ')
    b = {}
    for key in a:
        b[key] = b.get(key, 0) + 1
    return b


z = 'today this word bad better hello hello this'
print(count(z))
