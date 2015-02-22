
__problem_title__ = "Prime generating integers"
__problem_url___ = "https://projecteuler.net/problem=357"
__problem_description__ = "Consider the divisors of 30: 1,2,3,5,6,10,15,30. It can be seen that " \
                          "for every divisor of 30, +30/ is prime. Find the sum of all positive " \
                          "integers not exceeding 100 000 000 such that for every divisor of , + " \
                          "/ is prime."

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

