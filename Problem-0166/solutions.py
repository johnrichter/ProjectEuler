
__problem_title__ = "Criss Cross"
__problem_url___ = "https://projecteuler.net/problem=166"
__problem_description__ = "A 4x4 grid is filled with digits d, 0 ≤ d ≤ 9. It can be seen that in " \
                          "the grid 6 3 3 0 5 0 4 3 0 7 1 4 1 2 4 5 the sum of each row and each " \
                          "column has the value 12. Moreover the sum of each diagonal is also " \
                          "12. In how many ways can you fill a 4x4 grid with the digits d, 0 ≤ d " \
                          "≤ 9 so that each row, each column, and both diagonals have the same " \
                          "sum?"

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

