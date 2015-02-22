
__problem_title__ = "Rectangles in cross-hatched grids"
__problem_url___ = "https://projecteuler.net/problem=147"
__problem_description__ = "In a 3x2 cross-hatched grid, a total of 37 different rectangles could " \
                          "be situated within that grid as indicated in the sketch. There are 5 " \
                          "grids smaller than 3x2, vertical and horizontal dimensions being " \
                          "important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is " \
                          "cross-hatched, the following number of different rectangles could be " \
                          "situated within those smaller grids: 1x1: 1 2x1: 4 3x1: 8 1x2: 4 2x2: " \
                          "18 Adding those to the 37 of the 3x2 grid, a total of 72 different " \
                          "rectangles could be situated within 3x2 and smaller grids. How many " \
                          "different rectangles could be situated within 47x43 and smaller " \
                          "grids?"

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

