
__problem_title__ = "Largest integer divisible by two primes"
__problem_url___ = "https://projecteuler.net/problem=347"
__problem_description__ = "The largest integer ≤ 100 that is only divisible by both the primes 2 " \
                          "and 3 is 96, as 96=32*3=2 *3. For two primes p and q let M(p,q,N) be " \
                          "the largest positive integer ≤N only divisible by both p and q and " \
                          "M(p,q,N)=0 if such a positive integer does not exist. E.g. " \
                          "M(2,3,100)=96. M(3,5,100)=75 and not 90 because 90 is divisible by 2 " \
                          ",3 and 5. Also M(2,73,100)=0 because there does not exist a positive " \
                          "integer ≤ 100 that is divisible by both 2 and 73. Let S(N) be the sum " \
                          "of all distinct M(p,q,N). S(100)=2262. Find S(10 000 000)."

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

