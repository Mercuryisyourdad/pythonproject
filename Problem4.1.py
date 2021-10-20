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
    m, c, L = 0, 0, 0.001
    x = [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    print(gradient_descent(x,y,200))
    print(gradient_descent(x,y,500))
    print(gradient_descent(x,y,1000))
    print(gradient_descent(x,y,2000))
    print(gradient_descent(x,y,3000))