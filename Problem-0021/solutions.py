
__problem_title__ = "Amicable numbers"
__problem_url___ = "https://projecteuler.net/problem=21"
__problem_description__ = "Let d( ) be defined as the sum of proper divisors of (numbers less " \
                          "than which divide evenly into ). If d( ) = and d( ) = , where ≠ , " \
                          "then and are an amicable pair and each of and are called amicable " \
                          "numbers. For example, the proper divisors of 220 are 1, 2, 4, 5, 10, " \
                          "11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper " \
                          "divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220. Evaluate " \
                          "the sum of all the amicable numbers under 10000."

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

