# N-Queen_Solver-Genetic_algorithm

# Description:
Basic Solver For N-Queen Puzzle using Genetic Algorithm, AI

# Problem Statement
The problem is to place n - queens in such a manner on an n x n chessboard that no queens attack each other by being in the same row, column or diagonal.

# Solution Steps
i. It can be seen that for n =1, the problem has a trivial solution, and no solution exists for n =2 and n =3. So first we will consider the 4 queens problem and then generate it to n - queens problem.
ii. Using Genetic Algorithm to get desired state from randomly generated population and finding fitness value for each chromosome
iii. Implementation is done with python
iv. Population is an array where each element of it is an array itself [Means each chromosome is an array of vertical position of the Queen]
v. Used Libraries: random, sys

# Computation Threshold is 0.03


# Sample Output
Enter Number of Queens: 8

Dimension :  8 X 8 
Population :  10 

Enter Maximun Generation Count: 20000

Generation : [============================                      ]  57% > Count: 11545

Solution :  [8, 2, 4, 1, 7, 5, 3, 6]

Solution Board:
⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜
⬜ ⬜ ⬜ ⬜ ⬛ ⬜ ⬜ ⬜
⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛
⬜ ⬜ ⬜ ⬜ ⬜ ⬛ ⬜ ⬜
⬜ ⬜ ⬛ ⬜ ⬜ ⬜ ⬜ ⬜
⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ ⬜
⬜ ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜
⬜ ⬜ ⬜ ⬛ ⬜ ⬜ ⬜ ⬜
