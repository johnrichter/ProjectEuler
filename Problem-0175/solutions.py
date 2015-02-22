
__problem_title__ = "Fractions involving the number of different ways a number can be expressed as a sum of powers of 2"
__problem_url___ = "https://projecteuler.net/problem=175"
__problem_description__ = ""

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

