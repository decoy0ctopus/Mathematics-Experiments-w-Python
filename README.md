# Mathematics-Experiments-w-Python

Exercises from the book 'MATH ADVENTURES WITH PYTHON: AN ILLUSTRATED GUIDE TO EXPLORING MATH WITH CODE' by Peter Farrell

Uses the processing module for graphical displays, Go to https://processing.org/download/ and choose your operating system

# Colour Grid

Simple test to create blocks of colour

# Geometry Processing

Test file of basic geometry tooling

# Harmonograph

Python-Processing sketch that models the movement of a pendulum

# Julia

The Julia set is constructed just like the Mandelbrot set, but after squaring the complex number, instead of adding the original complex number of that point, we keep adding a constant complex number, c, which has the same value for all points. By starting with different values for c, we can create lots of different Julia sets.

![f142-01](https://user-images.githubusercontent.com/64989388/166318147-800b524f-27d3-4122-a86a-e72b36809237.jpg)

The Julia set for c = –0.8 + 0.156 i

# Mandelbrot

The mandelbrot() function takes a complex number, z, and a number of iterations as parameters. It returns the number of times it took for z to diverge, and if it never diverges, it returns num (at the end of the function). We create a count variable ➊ to keep track of the iterations, and we create a new complex number, z1, that gets squared and so on without changing z.

We start a loop to repeat the process while the count variable is less than num ➋. Inside the loop we check the magnitude of z1 to see whether z1 has diverged, and if it has, we return count and stop the code. Otherwise, we square z1 and add z to it ➌, which is the definition of our operation on complex numbers. Finally, we increment the count variable by 1 and loop through the process again.

![f140-01](https://user-images.githubusercontent.com/64989388/166318591-b5d38d35-cd6c-4b89-bc0c-6e0ddc330f70.jpg)

# Matrices & Matrices3D

Basic functions for creating and manipulating mathematical matrices in different dimensions.

# Polygon

Functions for creating polygons and spirographs




