
__problem_title__ = "How many reversible numbers are there below one-billion?"
__problem_url___ = "https://projecteuler.net/problem=145"
__problem_description__ = "Some positive integers have the property that the sum [ + reverse( ) " \
                          "] consists entirely of odd (decimal) digits. For instance, 36 + 63 = " \
                          "99 and 409 + 904 = 1313. We will call such numbers ; so 36, 63, 409, " \
                          "and 904 are reversible. Leading zeroes are not allowed in either or " \
                          "reverse( ). There are 120 reversible numbers below one-thousand. How " \
                          "many reversible numbers are there below one-billion (10 )?"

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

