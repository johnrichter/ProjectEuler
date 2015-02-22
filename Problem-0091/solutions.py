
__problem_title__ = "Right triangles with integer coordinates"
__problem_url___ = "https://projecteuler.net/problem=91"
__problem_description__ = "The points P ( , ) and Q ( , ) are plotted at integer co-ordinates " \
                          "and are joined to the origin, O(0,0), to form ΔOPQ. There are exactly " \
                          "fourteen triangles containing a right angle that can be formed when " \
                          "each co-ordinate lies between 0 and 2 inclusive; that is, 0 ≤ , , , ≤ " \
                          "2. Given that 0 ≤ , , , ≤ 50, how many right triangles can be formed?"

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

