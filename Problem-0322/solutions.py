
__problem_title__ = "Binomial coefficients divisible by 10"
__problem_url___ = "https://projecteuler.net/problem=322"
__problem_description__ = "Let T( , ) be the number of the binomial coefficients C that are " \
                          "divisible by 10 for ≤ < ( , and are positive integers). You are given " \
                          "that T(10 , 10 -10) = 989697000. Find T(10 , 10 -10)."

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

