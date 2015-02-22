
__problem_title__ = "Red, green, and blue tiles"
__problem_url___ = "https://projecteuler.net/problem=117"
__problem_description__ = "Using a combination of black square tiles and oblong tiles chosen " \
                          "from: red tiles measuring two units, green tiles measuring three " \
                          "units, and blue tiles measuring four units, it is possible to tile a " \
                          "row measuring five units in length in exactly fifteen different ways. " \
                          "How many ways can a row measuring fifty units in length be tiled? " \
                          "NOTE: This is related to ."

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

