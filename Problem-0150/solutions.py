
__problem_title__ = "Searching a triangular array for a sub-triangle having minimum-sum"
__problem_url___ = "https://projecteuler.net/problem=150"
__problem_description__ = "In a triangular array of positive and negative integers, we wish to " \
                          "find a sub-triangle such that the sum of the numbers it contains is " \
                          "the smallest possible. In the example below, it can be easily " \
                          "verified that the marked triangle satisfies this condition having a " \
                          "sum of −42. We wish to make such a triangular array with one thousand " \
                          "rows, so we generate 500500 pseudo-random numbers in the range ±2 , " \
                          "using a type of random number generator (known as a Linear " \
                          "Congruential Generator) as follows: := 0 for k = 1 up to k = 500500: " \
                          ":= (615949* + 797807) modulo 2 := −2 Thus: = 273519, = −153582, = " \
                          "450905 etc Our triangular array is then formed using the " \
                          "pseudo-random numbers thus: Sub-triangles can start at any element of " \
                          "the array and extend down as far as we like (taking-in the two " \
                          "elements directly below it from the next row, the three elements " \
                          "directly below from the row after that, and so on). The "sum of a " \
                          "sub-triangle" is defined as the sum of all the elements it contains. " \
                          "Find the smallest possible sub-triangle sum."

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

