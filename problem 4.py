def gradient_descent(x, y, epochs, m=0, c=0, L=0.001):
    def mean(con):
        s = 0
        for i in con:
            s += i
        return s / len(con)

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


if __name__ == '__main__':
    m, c, L = 0, 0, 0.001
    x = [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    epochs_list = [200, 500, 1000, 2000, 3000]
    for epochs in epochs_list:
        ans = gradient_descent(x, y, epochs)
        print("epochs: {epochs}; m: {m}; c: {c}".format(epochs=epochs, m=ans[0], c=ans[1]))
