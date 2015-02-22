
__problem_title__ = "Enmeshed unit circle"
__problem_url___ = "https://projecteuler.net/problem=392"
__problem_description__ = "A rectilinear grid is an orthogonal grid where the spacing between " \
                          "the gridlines does not have to be equidistant. An example of such " \
                          "grid is logarithmic graph paper. Consider rectilinear grids in the " \
                          "Cartesian coordinate system with the following properties: E.g. here " \
                          "is a picture of the solution for N = 10: Find the positions for N = " \
                          "400. Give as your answer the area occupied by the red cells rounded " \
                          "to 10 digits behind the decimal point."

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

