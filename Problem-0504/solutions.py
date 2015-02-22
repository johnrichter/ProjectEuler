
__problem_title__ = "Square on the Inside"
__problem_url___ = "https://projecteuler.net/problem=504"
__problem_description__ = "Let be a quadrilateral whose vertices are lattice points lying on the " \
                          "coordinate axes as follows: ( , 0), (0, ), ( , 0), (0, ), where 1 ≤ , " \
                          ", , ≤ and , , , , are integers. It can be shown that for = 4 there " \
                          "are exactly 256 valid ways to construct . Of these 256 " \
                          "quadrilaterals, 42 of them contain a square number of lattice points. " \
                          "How many quadrilaterals strictly contain a square number of lattice " \
                          "points for = 100?"

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

