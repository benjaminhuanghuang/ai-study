'''
    Suppose the hypothesis function is h(x) = theta0 + theta1*x
    the loss function is J(theta) = 1/2* m * sum(h(x) - y) ** 2 

    reference:
        https://www.cnblogs.com/sumai/p/5211558.html
'''



# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from numpy.linalg import inv
from numpy import dot
 
iris = pd.read_csv('database/iris.csv')

temp = iris.iloc[:, 1:4]
temp['x0'] = 1
X = temp.iloc[:,[3,0,1,2]]
Y = iris.iloc[:, 0]
Y = Y.reshape(len(iris), 1)
theta_n = dot(dot(inv(dot(X.T, X)), X.T), Y) # theta = (X'X)^(-1)X'Y
print(theta_n)

#批量梯度下降法
theta_g = np.array([1., 1., 1., 1.]) #初始化theta
theta_g = theta_g.reshape(4, 1)
alpha = 0.1
temp = theta_g
X0 = X.iloc[:, 0].reshape(150, 1)
X1 = X.iloc[:, 1].reshape(150, 1)
X2 = X.iloc[:, 2].reshape(150, 1)
X3 = X.iloc[:, 3].reshape(150, 1)
J = pd.Series(np.arange(800, dtype = float))
for i in range(800):
    temp[0] = theta_g[0] + alpha*np.sum((Y- dot(X, theta_g))*X0)/150.
    temp[1] = theta_g[1] + alpha*np.sum((Y- dot(X, theta_g))*X1)/150.
    temp[2] = theta_g[2] + alpha*np.sum((Y- dot(X, theta_g))*X2)/150.
    temp[3] = theta_g[3] + alpha*np.sum((Y- dot(X, theta_g))*X3)/150.
    J[i] = 0.5*np.sum((Y - dot(X, theta_g))**2) #计算损失函数值    
    theta_g = temp #更新theta
    
print(theta_g)
print(J.plot(ylim = [0, 50]))