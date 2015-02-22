
__problem_title__ = "Multiples of 3 and 5"
__problem_url___ = "https://projecteuler.net/problem=1"
__problem_description__ = "If we list all the natural numbers below 10 that are multiples of 3 " \
                          "or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find " \
                          "the sum of all the multiples of 3 or 5 below 1000."

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

