
__problem_title__ = "Perfection Quotients"
__problem_url___ = "https://projecteuler.net/problem=241"
__problem_description__ = "For a positive integer , let σ( ) be the sum of all divisors of , so " \
                          "e.g. σ(6) = 1 + 2 + 3 + 6 = 12. A perfect number, as you probably " \
                          "know, is a number with σ( ) = 2 . Find the sum of all positive " \
                          "integers ≤ 10 for which ( ) has the form + ⁄ , where is an integer."

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

