
__problem_title__ = "Red, green or blue tiles"
__problem_url___ = "https://projecteuler.net/problem=116"
__problem_description__ = "A row of five black square tiles is to have a number of its tiles " \
                          "replaced with coloured oblong tiles chosen from red (length two), " \
                          "green (length three), or blue (length four). If red tiles are chosen " \
                          "there are exactly seven ways this can be done. If green tiles are " \
                          "chosen there are three ways. And if blue tiles are chosen there are " \
                          "two ways. Assuming that colours cannot be mixed there are 7 + 3 + 2 = " \
                          "12 ways of replacing the black tiles in a row measuring five units in " \
                          "length. How many different ways can the black tiles in a row " \
                          "measuring fifty units in length be replaced if colours cannot be " \
                          "mixed and at least one coloured tile must be used? NOTE: This is " \
                          "related to ."

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

