
__problem_title__ = "Prime summations"
__problem_url___ = "https://projecteuler.net/problem=77"
__problem_description__ = "It is possible to write ten as the sum of primes in exactly five " \
                          "different ways: 7 + 3 5 + 5 5 + 3 + 2 3 + 3 + 2 + 2 2 + 2 + 2 + 2 + 2 " \
                          "What is the first value which can be written as the sum of primes in " \
                          "over five thousand different ways?"

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

