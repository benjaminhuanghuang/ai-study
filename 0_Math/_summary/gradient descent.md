
梯度下降法就是快速找到最低点的方法：
方向： 梯度的反方向
距离： 学习率
终止条件：梯度的模小于某个值

## The rules
```
y = t * x^a
y' = t * a * x^(a-1)


f(x) = f1(x) + f2(x)
f'(x) = f1'(x) + f2'(x)
```

梯度可以定义为一个函数全部偏导数构成的向量，梯度向量的方向是函数值变化率最大的方向，梯度向量的模是函数值变化率最大的值。
```
    f(x, y) = x^2 + y^2

    gradient descent = [2x, 2y]

```



## Reference
![Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8)

https://www.youtube.com/watch?v=UkcUZTe49Pg

https://www.youtube.com/watch?v=s7BxboxEfnU
