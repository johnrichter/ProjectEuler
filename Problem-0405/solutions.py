
__problem_title__ = "A rectangular tiling"
__problem_url___ = "https://projecteuler.net/problem=405"
__problem_description__ = "We wish to tile a rectangle whose length is twice its width. Let (0) " \
                          "be the tiling consisting of a single rectangle. For > 0, let ( ) be " \
                          "obtained from ( -1) by replacing all tiles in the following manner: " \
                          "The following animation demonstrates the tilings ( ) for from 0 to 5: " \
                          "Let ( ) be the number of points where four tiles meet in ( ). For " \
                          "example, (1) = 0, (4) = 82 and (10 ) mod 17 = 126897180. Find (10 ) " \
                          "for = 10 , give your answer modulo 17 ."

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

