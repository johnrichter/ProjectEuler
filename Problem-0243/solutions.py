
__problem_title__ = "Resilience"
__problem_url___ = "https://projecteuler.net/problem=243"
__problem_description__ = "A positive fraction whose numerator is less than its denominator is " \
                          "called a proper fraction. For any denominator, , there will be −1 " \
                          "proper fractions; for example, with = 12: / , / , / , / , / , / , / , " \
                          "/ , / , / , / . We shall call a fraction that cannot be cancelled " \
                          "down a . Furthermore we shall define the of a denominator, ( ), to be " \
                          "the ratio of its proper fractions that are resilient; for example, " \
                          "(12) = / . In fact, = 12 is the smallest denominator having a " \
                          "resilience ( ) 4/ . Find the smallest denominator , having a " \
                          "resilience ( ) 15499/ ."

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

