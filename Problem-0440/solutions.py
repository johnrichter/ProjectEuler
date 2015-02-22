
__problem_title__ = "GCD and Tiling"
__problem_url___ = "https://projecteuler.net/problem=440"
__problem_description__ = "We want to tile a board of length and height 1 completely, with " \
                          "either 1 × 2 blocks or 1 × 1 blocks with a single decimal digit on " \
                          "top: For example, here are some of the ways to tile a board of length " \
                          "= 8: Let T( ) be the number of ways to tile a board of length as " \
                          "described above. For example, T(1) = 10 and T(2) = 101. Let S( ) be " \
                          "the triple sum ∑ gcd(T( ), T( )) for 1 ≤ , , ≤ . For example: S(2) = " \
                          "10444 S(3) = 1292115238446807016106539989 S(4) mod 987 898 789 = " \
                          "670616280. Find S(2000) mod 987 898 789."

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

