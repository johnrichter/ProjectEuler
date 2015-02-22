
__problem_title__ = "RSA encryption"
__problem_url___ = "https://projecteuler.net/problem=182"
__problem_description__ = "The RSA encryption is based on the following procedure: Generate two " \
                          "distinct primes and . Compute and φ=( -1)( -1). Find an integer , 1< " \
                          "<φ, such that gcd( ,φ)=1. A message in this system is a number in the " \
                          "interval [0, -1]. A text to be encrypted is then somehow converted to " \
                          "messages (numbers in the interval [0, -1]). To encrypt the text, for " \
                          "each message, , = mod is calculated. To decrypt the text, the " \
                          "following procedure is needed: calculate such that =1 mod φ, then for " \
                          "each encrypted message, , calculate mod . There exist values of and " \
                          "such that mod . We call messages for which mod unconcealed messages. " \
                          "An issue when choosing is that there should not be too many " \
                          "unconcealed messages. For instance, let =19 and =37. Then =19*37=703 " \
                          "and φ=18*36=648. If we choose =181, then, although gcd(181,648)=1 it " \
                          "turns out that all possible messages (0≤ ≤ -1) are unconcealed when " \
                          "calculating mod . For any valid choice of there exist some " \
                          "unconcealed messages. It's important that the number of unconcealed " \
                          "messages is at a minimum. Choose =1009 and =3643. Find the sum of all " \
                          "values of , 1< <φ(1009,3643) and gcd( ,φ)=1, so that the number of " \
                          "unconcealed messages for this value of is at a minimum."

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

