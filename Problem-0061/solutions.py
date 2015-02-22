
__problem_title__ = "Cyclical figurate numbers"
__problem_url___ = "https://projecteuler.net/problem=61"
__problem_description__ = "Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal " \
                          "numbers are all figurate (polygonal) numbers and are generated by the " \
                          "following formulae: The ordered set of three 4-digit numbers: 8128, " \
                          "2882, 8281, has three interesting properties. Find the sum of the " \
                          "only ordered set of six cyclic 4-digit numbers for which each " \
                          "polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, " \
                          "and octagonal, is represented by a different number in the set."

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
