
__problem_title__ = "Cubic permutations"
__problem_url___ = "https://projecteuler.net/problem=62"
__problem_description__ = "The cube, 41063625 (345 ), can be permuted to produce two other " \
                          "cubes: 56623104 (384 ) and 66430125 (405 ). In fact, 41063625 is the " \
                          "smallest cube which has exactly three permutations of its digits " \
                          "which are also cube. Find the smallest cube for which exactly five " \
                          "permutations of its digits are cube."

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

