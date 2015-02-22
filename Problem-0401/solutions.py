
__problem_title__ = "Sum of squares of divisors"
__problem_url___ = "https://projecteuler.net/problem=401"
__problem_description__ = "The divisors of 6 are 1,2,3 and 6. The sum of the squares of these " \
                          "numbers is 1+4+9+36=50. Let sigma2(n) represent the sum of the " \
                          "squares of the divisors of n. Thus sigma2(6)=50. Find SIGMA2(10 ) " \
                          "modulo 10 ."

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

