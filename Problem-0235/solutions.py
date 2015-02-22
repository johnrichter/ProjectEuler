
__problem_title__ = "An Arithmetic Geometric sequence"
__problem_url___ = "https://projecteuler.net/problem=235"
__problem_description__ = "Given is the arithmetic-geometric sequence u( ) = (900-3 ) . Let s( ) " \
                          "= Σ u( ). Find the value of for which s(5000) = -600,000,000,000. " \
                          "Give your answer rounded to 12 places behind the decimal point."

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

