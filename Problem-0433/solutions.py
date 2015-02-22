
__problem_title__ = "Steps in Euclid's algorithm"
__problem_url___ = "https://projecteuler.net/problem=433"
__problem_description__ = "Let E( , ) be the number of steps it takes to determine the greatest " \
                          "common divisor of and with . More formally: = , = mod = , = mod E( , " \
                          ") is the smallest such that = 0. We have E(1,1) = 1, E(10,6) = 3 and " \
                          "E(6,10) = 4. Define S(N) as the sum of E( ) for 1 ≤ ≤ N. We have S(1) " \
                          "= 1, S(10) = 221 and S(100) = 39826. Find S(5·10 )."

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

