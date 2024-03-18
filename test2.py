import numpy as np
import colors as bcolors
import math


# from matrix_utility import ...

from inverse_matrix import inverse
from gauss_seidel import gauss_seidel
from Jacobi import jacobi_iterative

from lu import lu
from lu import backward_substitution
from lu import lu_solve

from gaussian_elimination import gaussianElimination
from gaussian_elimination import backward_substitution
from gaussian_elimination import forward_substitution


from condition_of_linear_equations import condition_number
from condition_of_linear_equations import norm

from iterative_method import find_roots_iterative_method
from iterative_method import iterative_method
from bisection_method import bisection_method


# def input(mat):
#     result = gaussianElimination(mat)
#     f = lambda x: (math.exp(1)*x**5 - 3*x**3 + 2*x**2 + 1)/3*x
#     roots = bisection_method(f, -2, 2)
#     print(f"\nThe equation f(x) has an approximate root at x = {roots}")
#     # f = lambda x: x ** 2 - 4
#     # for i in range (-100,100, 1):
#     #     roots = bisection_method(f, i, i+4)
#     #     print(f"\nThe equation f(x) has an approximate root at x = {roots}" )
#     # return result
#     return

def output():
    print("Date:18/3/24\n"
          "Group members: \n"
          "(1) name: Shulamit-mor-yossef. id: 206576977. \n"
          "(2) name: Zohar-monsonego. id: 214067662. \n"
          "(3) name: hodaya-shirazie. id: 213907785.\n"
          "Git: https://github.com/shulamitmorjossef/test2-shulamit.git\n"
          "Name: Shulamit Mor Yossef, 206576977.\n"

          "input:    \n[[-1, 1, 3, -3, 1,3],\n"
           "[3, -3, -4, 2, 3, 8],\n"
           "[2, 1, -5, -3, 5, 2],\n"
           "[-5, -6, 4, 1, 3, 14],\n"
           "[3, -2, -2, -3, 5, 6]]\n")
    print("output:\n ")
    print("The matrix solution: \n")


    A_b = [[-1, 1, 3, -3, 1,3],
           [3, -3, -4, 2, 3, 8],
           [2, 1, -5, -3, 5, 2],
           [-5, -6, 4, 1, 3, 14],
           [3, -2, -2, -3, 5, 6]]
    result = gaussianElimination(A_b)
    if isinstance(result, str):
        print(result)
    else:
        print("\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))

    print("\n\n\nThe roots: \n")
    f = lambda x: (math.exp(1) * x ** 5 - 3 * x ** 3 + 2 * x ** 2 + 1) / 3 * x
    # roots = bisection_method(f, 0, 2)
    # print(f"\nRoot: {roots}")
    roots = bisection_method(f, -2, 0)
    print(f"\nRoot: {roots}")
    # for i in range (-2,2, 1):
    #     initial_guess = i
    #     root, iterations = iterative_method(f, initial_guess, -2, 2)  # Adjust lower and upper bounds as needed
    #     if root is not None:
    #         print(f"\nRoot:", root)
    initial_guess = -2
    root, iterations = iterative_method(f, initial_guess, -2, 2)  # Adjust lower and upper bounds as needed
    if root is not None:
        print(f"\nRoot:", root)
    return


if __name__ == '__main__':

    output()
