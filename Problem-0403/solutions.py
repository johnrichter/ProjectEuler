
__problem_title__ = "Lattice points enclosed by parabola and line"
__problem_url___ = "https://projecteuler.net/problem=403"
__problem_description__ = "For integers and , we define ( , ) as the domain enclosed by the " \
                          "parabola = and the line = · + : ( , ) = { ( , ) | ≤ ≤ · + }. L( , ) " \
                          "is defined as the number of lattice points contained in ( , ). For " \
                          "example, L(1, 2) = 8 and L(2, -1) = 1. We also define S( ) as the sum " \
                          "of L( , ) for all the pairs ( , ) such that the area of ( , ) is a " \
                          "rational number and | |,| | ≤ . We can verify that S(5) = 344 and " \
                          "S(100) = 26709528. Find S(10 ). Give your answer mod 10 ."

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

