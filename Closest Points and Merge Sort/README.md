Closest-Points Problem: We know that the Euclidean distance between any two points on a plane,
say (a1; b1) and (a2; b2) is
square_root((a2 - a1)^2 + (b2 - b1)^2)

Write a program that takes as input from keyboard
the value of a positive integer N, and the coordinates of N points on the 2-dimensional plane, namely
(x1; y1); (x2; y2); . . .  ; (xn; yn). The program then finds a closest pair of points and outputs this pair of
points along with the distance between them. It is possible that two points have the same position;
in that case, that pair is the closest, with distance zero. The program should print the output on the
standard output. You may round real numbers to two decimal places.
Input/Output format explained using an example:

How many points are there on the 2D plane? 3
Enter the coordinates of Point 1
x1 : 3
y1 : 2
Enter the coordinates of Point 2
x2 : 2
y2 : 0
Enter the coordinates of Point 3
x3 : 3
y3 : 3:5

The closest pair of points are (3; 2) and (3; 3.5). The distance between them is 1.5 units.
0.2 Outline of the Algorithm to be Used
Go to Section 10.2.2 (page 470) of the book Data Structures and Algorithm Analysis in C++
(DSAAC)", by MARK ALLEN WEISS.

You are expected to implement the divide and conquer
algorithm for the "Closest-Points Problem" outlined in this section. This algorithm, given N points,
finds a closest pair of points in O(N logN) time.

Program Related Instructions :

1. You can write your program in one of C, C++, Java, or Python.

2. The main divide and conquer algorithm described in Section 10.2.2 of DSAAC involves sorting N
numbers in (N logN) time. You are expected to write the code for a MERGE SORT algorithm
from scratch for sorting purposes.
