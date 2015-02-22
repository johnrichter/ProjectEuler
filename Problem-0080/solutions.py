
__problem_title__ = "Square root digital expansion"
__problem_url___ = "https://projecteuler.net/problem=80"
__problem_description__ = "It is well known that if the square root of a natural number is not " \
                          "an integer, then it is irrational. The decimal expansion of such " \
                          "square roots is infinite without any repeating pattern at all. The " \
                          "square root of two is 1.41421356237309504880..., and the digital sum " \
                          "of the first one hundred decimal digits is 475. For the first one " \
                          "hundred natural numbers, find the total of the digital sums of the " \
                          "first one hundred decimal digits for all the irrational square roots."

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

