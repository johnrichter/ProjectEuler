
__problem_title__ = "Counting rectangles"
__problem_url___ = "https://projecteuler.net/problem=85"
__problem_description__ = "By counting carefully it can be seen that a rectangular grid " \
                          "measuring 3 by 2 contains eighteen rectangles: Although there exists " \
                          "no rectangular grid that contains exactly two million rectangles, " \
                          "find the area of the grid with the nearest solution."

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

