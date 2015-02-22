
__problem_title__ = "Hexagonal orchards"
__problem_url___ = "https://projecteuler.net/problem=351"
__problem_description__ = "A of order is a triangular lattice made up of points within a regular " \
                          "hexagon with side . The following is an example of a hexagonal " \
                          "orchard of order 5: Highlighted in green are the points which are " \
                          "hidden from the center by a point closer to it. It can be seen that " \
                          "for a hexagonal orchard of order 5, 30 points are hidden from the " \
                          "center. Let H( ) be the number of points hidden from the center in a " \
                          "hexagonal orchard of order . H(5) = 30. H(10) = 138. H(1 000) = " \
                          "1177848. Find H(100 000 000)."

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

