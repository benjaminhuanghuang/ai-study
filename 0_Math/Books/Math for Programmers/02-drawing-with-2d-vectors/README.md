## Introduction 
- linear transformation
A linear transformation is a kind of function that takes a vector as input and returns a vector as output, while preserving the geometry (in a special sense) of the vectors involved. 

## Vector
Vectors are objects that live in multi-dimensional spaces. 

A 2D vector is a point in the plane relative to the origin.

you can think of a vector as a straight arrow in the plane; any arrow can be placed to start at the origin, and it indicates a particular point

## 2D drawing in Python
Python has libraries like Pillow and Turtle that are well equipped for creating drawings with vector data

## Vector addition
```
def add(v1,v2):
    return (v1[0] + v2[0], v1[1] + v2[1])
```
The rule for vector addition of arrows is sometimes called tip-to-tail addition. That’s because if you move the tail of the second arrow to the tip of the first (without changing its length or direction!), then the sum is the arrow from the start of the first to the end of the second 

When we talk about arrows, we really mean “a specific distance in a specific direction.”

"Move or translate" a vector collection
```
    dino_vectors2 = [add((−1.5,−2.5), v) for v  in dino_vectors]


    def translate(translation, vectors):
        return [add(translation, v) for v  in vectors]
```


## Vector components and length
The two vectors (4, 0) and (0, 3) are called the x and y components,

## Multiplying vectors by scala/number
Repeated addition of vectors 

The operation of multiplying a vector by a number is called scalar multiplication .
the effect of this operation is scaling（放缩） the target vector by the given factor.

Scalar multiplication of a vector scales both components by the same factor.

## Subtraction
The opposite vector -v will have the same length, but it will point in the opposite direction.


```
def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i+1)%len(vectors)])
                 for i in range(0,len(vectors))]
    return sum(distances)
```

## Angles and trigonometry
Adding vectors is easier to use Cartesian coordinates. 
polar coordinates are more useful when we want to look at vectors rotated by some angle. 

polar coordinates to cartesian coordinates
```
    （r*cos(θ), r*sin(θ))


    from math import sin, cos

    def to_cartesian(polar_vector):
        length, angle = polar_vector[0], polar_vector[1]
        return (length*cos(angle), length*sin(angle))



    def to_polar(vector):
        x, y = vector[0], vector[1]
        # math.atan2 function takes the Cartesian coordinates of a point in the plane (in reverse order!)
        angle = atan2(y,x)
        return (length(vector), angle)    
```


## Transforming collections of vectors
moving (or translating) a collection of vectors is easy with Cartesian coordinates.

Polar coordinates have angles built in, these make it simple to carry out rotations.

Rotating a number of vectors simultaneously has the effect of rotating the figure these represent about the origin
```
def rotate(angle, vectors):
    polars = [to_polar(v) for v  in vectors]
    return [to_cartesian((l, a+angle)) for l,a in polars]
```
