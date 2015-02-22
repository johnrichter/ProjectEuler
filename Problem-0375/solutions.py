
__problem_title__ = "Minimum of subsequences"
__problem_url___ = "https://projecteuler.net/problem=375"
__problem_description__ = "Let be an integer sequence produced with the following pseudo-random " \
                          "number generator: Let A( , ) be the minimum of the numbers , , ... , " \
                          "for ≤ . Let M( ) = ΣA( , ) for 1 ≤ ≤ ≤ . We can verify that M(10) = " \
                          "432256955 and M(10 000) = 3264567774119. Find M(2 000 000 000)."

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

