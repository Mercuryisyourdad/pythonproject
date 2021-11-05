def gradient_descent(x, y, epochs, m=0, c=0, L=0.001):
    def cal_average(li):
        sum_ret = 0
        total_num = 0
        for num in li:
            sum_ret += num
            total_num += 1
        return sum_ret / total_num
    for i in range(epochs):
        dm, dc = [], []
        for j in range(len(x)):
            yp = x[j][0] * m + c
            dm.append(x[j][0] * (yp - y[j]))
            dc.append(yp - y[j])
        m = m - L * cal_average(dm)
        c = c - L * cal_average(dc)
    return m, c


def gradient_descent(x, y, m, c, epochs, L=0.001):
    def mean(con):
        sum = 0
        for i in con:
            sum += i
        return sum / len(con)

    for t in range(epochs):
        dm, dc = [], []
        for i in range(len(x)):
            xi = x[i][0]
            yi = y[i]
            yp = xi * m + c
            dm.append(xi * (yp - yi))
            dc.append(yp - yi)
        Dm = mean(dm)
        Dc = mean(dc)
        m = m - L * Dm
        c = c - L * Dc
    return m, c

