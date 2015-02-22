
__problem_title__ = "Retractions A"
__problem_url___ = "https://projecteuler.net/problem=445"
__problem_description__ = "For every integer n>1, the family of functions f is defined by f ( " \
                          ")≡a +b mod n for a,b, integer and 0<a<n, 0≤b<n, 0≤ <n. We will call f " \
                          "a if f (f ( ))≡f ( ) mod n for every 0≤ <n. Let R(n) be the number of " \
                          "retractions for n. You are given that ∑ R(c) for c=C(100 000,k), and " \
                          "1 ≤ k ≤99 999 ≡628701600 (mod 1 000 000 007). (C(n,k) is the binomial " \
                          "coefficient). Find ∑ R(c) for c=C(10 000 000,k), and 1 ≤k≤ 9 999 999. " \
                          "Give your answer modulo 1 000 000 007."

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

