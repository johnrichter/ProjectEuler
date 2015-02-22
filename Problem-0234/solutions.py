
__problem_title__ = "Semidivisible numbers"
__problem_url___ = "https://projecteuler.net/problem=234"
__problem_description__ = "For an integer ≥ 4, we define the of , denoted by lps( ), as the " \
                          "largest prime ≤ √ and the of , ups( ), as the smallest prime ≥ √ . " \
                          "So, for example, lps(4) = 2 = ups(4), lps(1000) = 31, ups(1000) = 37. " \
                          "Let us call an integer ≥ 4 , if one of lps( ) and ups( ) divides , " \
                          "but not both. The sum of the semidivisible numbers not exceeding 15 " \
                          "is 30, the numbers are 8, 10 and 12. 15 is not semidivisible because " \
                          "it is a multiple of both lps(15) = 3 and ups(15) = 5. As a further " \
                          "example, the sum of the 92 semidivisible numbers up to 1000 is 34825. " \
                          "What is the sum of all semidivisible numbers not exceeding " \
                          "999966663333 ?"

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

