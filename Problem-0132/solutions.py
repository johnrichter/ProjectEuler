
__problem_title__ = "Large repunit factors"
__problem_url___ = "https://projecteuler.net/problem=132"
__problem_description__ = "A number consisting entirely of ones is called a repunit. We shall " \
                          "define R( ) to be a repunit of length . For example, R(10) = " \
                          "1111111111 = 11×41×271×9091, and the sum of these prime factors is " \
                          "9414. Find the sum of the first forty prime factors of R(10 )."

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

