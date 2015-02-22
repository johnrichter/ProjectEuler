
__problem_title__ = "Counting block combinations II"
__problem_url___ = "https://projecteuler.net/problem=115"
__problem_description__ = "NOTE: This is a more difficult version of . A row measuring units in " \
                          "length has red blocks with a minimum length of units placed on it, " \
                          "such that any two red blocks (which are allowed to be different " \
                          "lengths) are separated by at least one black square. Let the " \
                          "fill-count function, F( , ), represent the number of ways that a row " \
                          "can be filled. For example, F(3, 29) = 673135 and F(3, 30) = 1089155. " \
                          "That is, for = 3, it can be seen that = 30 is the smallest value for " \
                          "which the fill-count function first exceeds one million. In the same " \
                          "way, for = 10, it can be verified that F(10, 56) = 880711 and F(10, " \
                          "57) = 1148904, so = 57 is the least value for which the fill-count " \
                          "function first exceeds one million. For = 50, find the least value of " \
                          "for which the fill-count function first exceeds one million."

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

