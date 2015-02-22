
__problem_title__ = "Solving the diophantine equation  / + / =  /  "
__problem_url___ = "https://projecteuler.net/problem=157"
__problem_description__ = "Consider the diophantine equation / + / = / with positive integers " \
                          "and ≤ . For =1 this equation has 20 solutions that are listed below: " \
                          "How many solutions has this equation for 1 ≤ ≤ 9?"

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

