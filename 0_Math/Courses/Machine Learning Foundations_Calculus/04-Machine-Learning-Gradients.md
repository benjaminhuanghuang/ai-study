

Optimization techniques are based on the gradient, which explains how a multivariable function is changing and in which direction.


## Gradient
Gradient: The derivative of a function that accepts a vector as an input

Calculate the gradient for a two-variable function f(x, y) using a formula:

## Directional gradient
unit vector * gradient


Find the gradient vector and maximum directional derivative of a function f(x, y).
1. Calculate the gradient vector of the function at a given point (x, y)
2. Calculate the partial derivatives of the function with respect to x and y


Know how the model performance changes with respect to each parameter

Calculate the partial derivative between our cost function and each weight using chain rule

Update these weights in an iterative process

Backpropagation is one of the ways we can train our model. It is the algorithm that backpropagates the errors from the output nodes to the input nodes. Instead of the directly computing the gradient of the cost function with respect to each individual weight, the backpropagation algorithm compute the gradient of the cost function via the chain rule and then computes the gradient layer by layer. 

The goal of backpropagation based on error calculation is to reduce the error rate as much as possible so that accurate output can be supplied
