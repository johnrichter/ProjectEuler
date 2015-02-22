
__problem_title__ = "Square root convergents"
__problem_url___ = "https://projecteuler.net/problem=57"
__problem_description__ = "It is possible to show that the square root of two can be expressed " \
                          "as an infinite continued fraction. √ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... " \
                          "))) = 1.414213... By expanding this for the first four iterations, we " \
                          "get: 1 + 1/2 = 3/2 = 1.5 1 + 1/(2 + 1/2) = 7/5 = 1.4 1 + 1/(2 + 1/(2 " \
                          "+ 1/2)) = 17/12 = 1.41666... 1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 " \
                          "= 1.41379... The next three expansions are 99/70, 239/169, and " \
                          "577/408, but the eighth expansion, 1393/985, is the first example " \
                          "where the number of digits in the numerator exceeds the number of " \
                          "digits in the denominator. In the first one-thousand expansions, how " \
                          "many fractions contain a numerator with more digits than denominator?"

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

