
__problem_title__ = "Factorials divisible by a huge integer"
__problem_url___ = "https://projecteuler.net/problem=320"
__problem_description__ = "Let N( ) be the smallest integer such that ! is divisible by ( !) Let " \
                          "S( )=∑N( ) for 10 ≤ ≤ . S(1000)=614538266565663. Find S(1 000 000) " \
                          "mod 10 ."

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

