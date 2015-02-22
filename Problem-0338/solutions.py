
__problem_title__ = "Cutting Rectangular Grid Paper"
__problem_url___ = "https://projecteuler.net/problem=338"
__problem_description__ = "A rectangular sheet of grid paper with integer dimensions × is given. " \
                          "Its grid spacing is 1. When we cut the sheet along the grid lines " \
                          "into two pieces and rearrange those pieces without overlap, we can " \
                          "make new rectangles with different dimensions. For example, from a " \
                          "sheet with dimensions 9 × 4 , we can make rectangles with dimensions " \
                          "18 × 2, 12 × 3 and 6 × 6 by cutting and rearranging as below: " \
                          "Similarly, from a sheet with dimensions 9 × 8 , we can make " \
                          "rectangles with dimensions 18 × 4 and 12 × 6 . For a pair and , let " \
                          "F( , ) be the number of distinct rectangles that can be made from a " \
                          "sheet with dimensions × . For example, F(2,1) = 0, F(2,2) = 1, F(9,4) " \
                          "= 3 and F(9,8) = 2. Note that rectangles congruent to the initial one " \
                          "are not counted in F( , ). Note also that rectangles with dimensions " \
                          "× and dimensions × are not considered distinct. For an integer , let " \
                          "G( ) be the sum of F( , ) for all pairs and which satisfy 0 < ≤ ≤ . " \
                          "We can verify that G(10) = 55, G(10 ) = 971745 and G(10 ) = " \
                          "9992617687. Find G(10 ). Give your answer modulo 10 ."

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

