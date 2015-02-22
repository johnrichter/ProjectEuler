
__problem_title__ = "Investigating the primality of numbers of the form 2 -1"
__problem_url___ = "https://projecteuler.net/problem=216"
__problem_description__ = "Consider numbers ( ) of the form ( ) = 2 -1 with > 1. The first such " \
                          "numbers are 7, 17, 31, 49, 71, 97, 127 and 161. It turns out that " \
                          "only 49 = 7*7 and 161 = 7*23 are not prime. For ≤ 10000 there are " \
                          "2202 numbers ( ) that are prime. How many numbers ( ) are prime for ≤ " \
                          "50,000,000 ?"

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

