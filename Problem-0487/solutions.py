
__problem_title__ = "Sums of power sums"
__problem_url___ = "https://projecteuler.net/problem=487"
__problem_description__ = "Let f ( ) be the sum of the powers of the first positive integers. " \
                          "For example, f (10) = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 385. " \
                          "Let S ( ) be the sum of f ( ) for 1 â¤ â¤ . For example, S (100) = " \
                          "35375333830. What is ∑ (S (10 ) mod p) over all primes between 2 â " \
                          "10 and 2 â 10 + 2000?"

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

