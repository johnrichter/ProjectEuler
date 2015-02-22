
__problem_title__ = "Primes with runs"
__problem_url___ = "https://projecteuler.net/problem=111"
__problem_description__ = "Considering 4-digit primes containing repeated digits it is clear " \
                          "that they cannot all be the same: 1111 is divisible by 11, 2222 is " \
                          "divisible by 22, and so on. But there are nine 4-digit primes " \
                          "containing three ones: 1117, 1151, 1171, 1181, 1511, 1811, 2111, " \
                          "4111, 8111 We shall say that M( , ) represents the maximum number of " \
                          "repeated digits for an -digit prime where is the repeated digit, N( , " \
                          ") represents the number of such primes, and S( , ) represents the sum " \
                          "of these primes. So M(4, 1) = 3 is the maximum number of repeated " \
                          "digits for a 4-digit prime where one is the repeated digit, there are " \
                          "N(4, 1) = 9 such primes, and the sum of these primes is S(4, 1) = " \
                          "22275. It turns out that for = 0, it is only possible to have M(4, 0) " \
                          "= 2 repeated digits, but there are N(4, 0) = 13 such cases. In the " \
                          "same way we obtain the following results for 4-digit primes. For = 0 " \
                          "to 9, the sum of all S(4, ) is 273700. Find the sum of all S(10, )."

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

