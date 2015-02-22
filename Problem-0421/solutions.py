
__problem_title__ = "Prime factors of  +1"
__problem_url___ = "https://projecteuler.net/problem=421"
__problem_description__ = "Numbers of the form +1 are composite for every integer > 1. For " \
                          "positive integers and let ( ) be defined as the sum of the prime " \
                          "factors of +1 not exceeding . Find &Sum; ( ,10 ) for 1 ≤ ≤ 10 ."

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

