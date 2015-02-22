
__problem_title__ = "Distinct terms in a multiplication table"
__problem_url___ = "https://projecteuler.net/problem=466"
__problem_description__ = "Let P( , ) be the number of terms in an × multiplication table. For " \
                          "example, a 3×4 multiplication table looks like this: There are 8 " \
                          "distinct terms {1,2,3,4,6,8,9,12}, therefore P(3,4) = 8. You are " \
                          "given that: P(64,64) = 1263, P(12,345) = 1998, and P(32,10 ) = " \
                          "13826382602124302. Find P(64,10 )."

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

