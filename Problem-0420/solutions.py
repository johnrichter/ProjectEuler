
__problem_title__ = "2x2 positive integer matrix"
__problem_url___ = "https://projecteuler.net/problem=420"
__problem_description__ = "A is a matrix whose elements are all positive integers. Some positive " \
                          "integer matrices can be expressed as a square of a positive integer " \
                          "matrix in two different ways. Here is an example: We define F( ) as " \
                          "the number of the 2x2 positive integer matrices which have a less " \
                          "than and which can be expressed as a square of a positive integer " \
                          "matrix in two different ways. We can verify that F(50) = 7 and " \
                          "F(1000) = 1019. Find F(10 )."

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

