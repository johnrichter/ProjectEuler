
__problem_title__ = "Lattice Quadrilaterals"
__problem_url___ = "https://projecteuler.net/problem=453"
__problem_description__ = "A is a polygon that has four distinct vertices, has no straight " \
                          "angles and does not self-intersect. Let Q(m, n) be the number of " \
                          "simple quadrilaterals whose vertices are lattice points with " \
                          "coordinates (x,y) satisfying 0 ≤ x ≤ m and 0 ≤ y ≤ n. For example, " \
                          "Q(2, 2) = 94 as can be seen below: It can also be verified that Q(3, " \
                          "7) = 39590, Q(12, 3) = 309000 and Q(123, 45) = 70542215894646. Find " \
                          "Q(12345, 6789) mod 135707531."

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

