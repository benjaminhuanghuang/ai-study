'''
 mean squared error (MSE) or mean squared deviation (MSD)

'''

import numpy as np


class LinearRegressor:
    def __init__(self, num_iteration, learning_rate, initial_m, initial_b):
        self.num_iteration = num_iteration
        self.learning_rate = learning_rate
        self.m = initial_m
        self.b = initial_b

    def train(self, data):
        for i in range(self.num_iteration):
            gradient_m, gradient_b = self.computGradient(data)
            self.m -= gradient_m * self.learning_rate
            self.b -= gradient_m * self.learning_rate

    def computGradient(self, data):
        total_gradient_m = 0
        total_gradient_b = 0
        for i in range(len(data)):
            x, y = data[i]
            predict_y = self.predict(x)
            gradient_m = 2 * x * (predict_y - y)
            gradient_b = 2 * (predict_y - y)

            total_gradient_m += gradient_m
        average_gradient_m = total_gradient_m / float(len(data))
        average_gradient_b = total_gradient_b / float(len(data))

        return average_gradient_m, average_gradient_b

    def predict(self, x):
        return self.m * x + self.b

    def computeMSE(self, data):
        total_error = 0
        for i in range(len(data)):
            x, y = data[i]
            predict_y = self.predict(x)
            error = (y - predict_y)**2
            total_error = error + total_error
        average_err = total_error / float(len(data))
        return average_err


def run():
    data = np.genfromtxt('../data/salary.csv', delimiter=',')

    # parameter
    num_iteration = 1000
    learning_rate = 0.0001
    initial_m = 0
    initial_b = 0

    model = LinearRegressor(num_iteration, learning_rate, initial_m, initial_b)
    print('MSE before training: ', model.computeMSE(data))

    model.train(data)
    print('MSE after training: ', model.computeMSE(data))
    print("m and b after training:", model.m, model.b)

if __name__ == '__main__':
    run()
