
__problem_title__ = "Distances in a bee's honeycomb "
__problem_url___ = "https://projecteuler.net/problem=354"
__problem_description__ = "Consider a honey bee's honeycomb where each cell is a perfect regular " \
                          "hexagon with side length 1. One particular cell is occupied by the " \
                          "queen bee. For a positive real number , let B( ) count the cells with " \
                          "distance from the queen bee cell (all distances are measured from " \
                          "centre to centre); you may assume that the honeycomb is large enough " \
                          "to accommodate for any distance we wish to consider. For example, " \
                          "B(√3) = 6, B(√21) = 12 and B(111 111 111) = 54. Find the number of ≤ " \
                          "5·10 such that B( ) = 450."

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

