
__problem_title__ = "Weak Goodstein sequence"
__problem_url___ = "https://projecteuler.net/problem=396"
__problem_description__ = "For any positive integer n, the {g , g , g , ...} is defined as: For " \
                          "example, the 6th weak Goodstein sequence is {6, 11, 17, 25, ...}: It " \
                          "can be shown that every weak Goodstein sequence terminates. Let G( ) " \
                          "be the number of nonzero elements in the th weak Goodstein sequence. " \
                          "It can be verified that G(2) = 3, G(4) = 21 and G(6) = 381. It can " \
                          "also be verified that ΣG( ) = 2517 for 1 ≤ < 8. Find the last 9 " \
                          "digits of ΣG( ) for 1 ≤ < 16."

import timeit


class Solution():

    @staticmethod
    def solution1():
        pass

    @staticmethod
    def time_solutions():
        setup = 'from __main__ import Solution'
        print('Solution 1:', timeit.timeit('Solution.solution1()', setup=setup, number=1))


if __name__ == '__main__':
    s = Solution()
    print(s.solution1())
    s.time_solutions()

