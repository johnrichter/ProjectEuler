
__problem_title__ = "The inverse summation of coprime couples"
__problem_url___ = "https://projecteuler.net/problem=441"
__problem_description__ = "For an integer , we define R( ) as the sum of 1/( · ) for all the " \
                          "integer pairs and which satisfy all of these conditions: We also " \
                          "define S( ) as the sum of R( ) for 2 ≤ ≤ . We can verify that S(2) = " \
                          "R(2) = 1/2, S(10) ≈ 6.9147 and S(100) ≈ 58.2962. Find S(10 ). Give " \
                          "your answer rounded to four decimal places."

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

