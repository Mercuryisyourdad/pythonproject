class LinearRegression(object):
    def __init__(self, x, y, m=0, c=0, epochs=200, lr=0.001):
        self.x = x
        self.y = y
        self.m = m
        self.c = c
        self.epochs = epochs
        self.lr = lr

    def gradientDescent(self):
        def mean(con):
            s = 0
            for i in con:
                s += i
            return s / len(con)

        for t in range(self.epochs):
            dm, dc = [], []
            for i in range(len(self.x)):
                xi = self.x[i][0]
                yi = self.y[i]
                yp = xi * self.m + self.c
                dm.append(xi * (yp - yi))
                dc.append(yp - yi)
            Dm = mean(dm)
            Dc = mean(dc)
            self.m = self.m - self.lr * Dm
            self.c = self.c - self.lr * Dc
        return self.m, self.c

    def predict(self, x):
        y = []
        for i in range(len(x)):
            y.append(self.m * x[i] + self.c)
        return y

if __name__ == '__main__':
    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    lr = LinearRegression(x, y, epochs=5000000)
    print(lr.gradientDescent())
    pre_y = lr.predictive(x)
    print(pre_y)