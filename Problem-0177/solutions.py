
__problem_title__ = "Integer angled Quadrilaterals"
__problem_url___ = "https://projecteuler.net/problem=177"
__problem_description__ = "Let ABCD be a convex quadrilateral, with diagonals AC and BD. At each " \
                          "vertex the diagonal makes an angle with each of the two sides, " \
                          "creating eight corner angles. For example, at vertex A, the two " \
                          "angles are CAD, CAB. We call such a quadrilateral for which all eight " \
                          "corner angles have integer values when measured in degrees an " \
                          ""integer angled quadrilateral". An example of an integer angled " \
                          "quadrilateral is a square, where all eight corner angles are 45°. " \
                          "Another example is given by DAC = 20°, BAC = 60°, ABD = 50°, CBD = " \
                          "30°, BCA = 40°, DCA = 30°, CDB = 80°, ADB = 50°. What is the total " \
                          "number of non-similar integer angled quadrilaterals? Note: In your " \
                          "calculations you may assume that a calculated angle is integral if it " \
                          "is within a tolerance of 10 of an integer value."

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

