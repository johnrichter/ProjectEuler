
__problem_title__ = "Divisibility comparison between factorials"
__problem_url___ = "https://projecteuler.net/problem=383"
__problem_description__ = "Let f ( ) be the largest integer for which 5 divides . For example, f " \
                          "(625000) = 7. Let T ( ) be the number of integers which satisfy f " \
                          "((2· -1)!) 5( !) and 1 ≤ ≤ . It can be verified that T (10 ) = 68 and " \
                          "T (10 ) = 2408210. Find T (10 )."

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

