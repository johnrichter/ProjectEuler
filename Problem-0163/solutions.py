
__problem_title__ = "Cross-hatched triangles"
__problem_url___ = "https://projecteuler.net/problem=163"
__problem_description__ = "Consider an equilateral triangle in which straight lines are drawn " \
                          "from each vertex to the middle of the opposite side, such as in the " \
                          "triangle in the sketch below. Sixteen triangles of either different " \
                          "shape or size or orientation or location can now be observed in that " \
                          "triangle. Using triangles as building blocks, larger triangles can be " \
                          "formed, such as the triangle in the above sketch. One-hundred and " \
                          "four triangles of either different shape or size or orientation or " \
                          "location can now be observed in that triangle. It can be observed " \
                          "that the triangle contains 4 triangle building blocks. A triangle " \
                          "would contain 9 triangle building blocks and a triangle would thus " \
                          "contain triangle building blocks. If we denote T( ) as the number of " \
                          "triangles present in a triangle of , then T(1) = 16 T(2) = 104 Find " \
                          "T(36)."

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

