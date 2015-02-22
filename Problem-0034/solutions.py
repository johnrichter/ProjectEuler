
__problem_title__ = "Digit factorials"
__problem_url___ = "https://projecteuler.net/problem=34"
__problem_description__ = "145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. Find " \
                          "the sum of all numbers which are equal to the sum of the factorial of " \
                          "their digits. Note: as 1! = 1 and 2! = 2 are not sums they are not " \
                          "included."

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

