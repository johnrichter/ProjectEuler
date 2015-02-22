
__problem_title__ = "Pythagorean Polygons"
__problem_url___ = "https://projecteuler.net/problem=292"
__problem_description__ = "We shall define a to be a with the following properties: For a given " \
                          "integer , define P( ) as the number of distinct pythagorean polygons " \
                          "for which the perimeter is ≤ . Pythagorean polygons should be " \
                          "considered distinct as long as none is a translation of another. You " \
                          "are given that P(4) = 1, P(30) = 3655 and P(60) = 891045. Find " \
                          "P(120)."

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

