import numpy as np
import colors as bcolors

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


def input(mat):
    result = gaussianElimination(mat)
    find_roots_iterative_method(result[0], result[1], result[2])
    return result

def output():
    print("Date:18/3/24\n"
          "Group members: \n"
          "(1) name: Shulamit-mor-yossef. id: 206576977. \n"
          "(2) name: Zohar-monsonego. id: 214067662. \n"
          "(3) name: hodaya-shirazie. id: 213907785.\n"
          "Git: https://github.com/shulamitmorjossef/test1\n"
          "Name: Shulamit Mor Yossef, 206576977.\n"

          "input:    \n[[1, 1/2, 1/3, 1]\n"
           "[1/2, 1/3, 1/4, 0]\n"
           "[1/3, 1/4, 1/5, 0]]\n")
    print("output:\n ")

    A_b = [[1, 1/2, 1/3, 1],
           [1/2, 1/3, 1/4, 0],
           [1/3, 1/4, 1/5, 0]]
    result = input(A_b)


    for x in result:
        print("{:.6f}".format(x))

    return
if __name__ == '__main__':

    output()
