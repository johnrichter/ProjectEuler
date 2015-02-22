
__problem_title__ = "Find the 200th prime-proof sqube containing the contiguous sub-string "200""
__problem_url___ = "https://projecteuler.net/problem=200"
__problem_description__ = "We shall define a sqube to be a number of the form, , where and are " \
                          "distinct primes. For example, 200 = 5 2 or 120072949 = 23 61 . The " \
                          "first five squbes are 72, 108, 200, 392, and 500. Interestingly, 200 " \
                          "is also the first number for which you cannot change any single digit " \
                          "to make a prime; we shall call such numbers, prime-proof. The next " \
                          "prime-proof sqube which contains the contiguous sub-string "200" is " \
                          "1992008. Find the 200th prime-proof sqube containing the contiguous " \
                          "sub-string "200"."

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

