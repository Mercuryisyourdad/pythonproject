def top_k_words(s, k):
    s = s.strip()
    z = ""
    for i in s:
        if i.isalpha() or i == ' ':
            z += i
    s = z
    li = s.split(' ')
    rng = []
    for i in li:
        if i != "":
            rng.append(i)
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
        res.append(max_key)  # 下来要把字典里的最大值删掉，让他循环第二大的值并取出 就显得很哇塞 就是很显得超级厉害
        edg.pop(max_key)
    return res


if __name__ == '__main__':
    print(top_k_words("   i love python, he    love coding python. the course is about python. ", 2))