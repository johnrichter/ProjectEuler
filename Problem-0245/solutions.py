
__problem_title__ = "Coresilience"
__problem_url___ = "https://projecteuler.net/problem=245"
__problem_description__ = "We shall call a fraction that cannot be cancelled down a resilient " \
                          "fraction. Furthermore we shall define the resilience of a " \
                          "denominator, ( ), to be the ratio of its proper fractions that are " \
                          "resilient; for example, (12) = ⁄ . Find the sum of all integers 1 < ≤ " \
                          "2×10 , for which ( ) is a ."

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

