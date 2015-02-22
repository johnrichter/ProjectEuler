
__problem_title__ = "Problem 500!!!"
__problem_url___ = "https://projecteuler.net/problem=500"
__problem_description__ = "The number of divisors of 120 is 16. In fact 120 is the smallest " \
                          "number having 16 divisors. Find the smallest number with 2 divisors. " \
                          "Give your answer modulo 500500507."

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

