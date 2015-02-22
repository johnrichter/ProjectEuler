
__problem_title__ = "Circumscribed Circles"
__problem_url___ = "https://projecteuler.net/problem=373"
__problem_description__ = "Every triangle has a circumscribed circle that goes through the three " \
                          "vertices. Consider all integer sided triangles for which the radius " \
                          "of the circumscribed circle is integral as well. Let S( ) be the sum " \
                          "of the radii of the circumscribed circles of all such triangles for " \
                          "which the radius does not exceed . S(100)=4950 and S(1200)=1653605. " \
                          "Find S(10 )."

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

