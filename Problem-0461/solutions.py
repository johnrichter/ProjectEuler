
__problem_title__ = "Almost Pi"
__problem_url___ = "https://projecteuler.net/problem=461"
__problem_description__ = "Let ( ) = - 1, for all non-negative integers . Remarkably, (6) + (75) " \
                          "+ (89) + (226) = 44529… ≈ . In fact, it is the best approximation of " \
                          "of the form ( ) + ( ) + ( ) + ( ) for = 200. Let ( ) = + + + for , , " \
                          ", that minimize the error: | ( ) + ( ) + ( ) + ( ) - | (where | | " \
                          "denotes the absolute value of ). You are given (200) = 6 + 75 + 89 + " \
                          "226 = 64658. Find (10000)."

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

