
__problem_title__ = "Euler's Number"
__problem_url___ = "https://projecteuler.net/problem=330"
__problem_description__ = "For example, Find A(10 ) + B(10 ) and give your answer mod 77 777 " \
                          "777."

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

