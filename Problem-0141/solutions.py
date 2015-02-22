
__problem_title__ = "Investigating progressive numbers,  , which are also square"
__problem_url___ = "https://projecteuler.net/problem=141"
__problem_description__ = "A positive integer, , is divided by and the quotient and remainder " \
                          "are and respectively. In addition , , and are consecutive positive " \
                          "integer terms in a geometric sequence, but not necessarily in that " \
                          "order. For example, 58 divided by 6 has quotient 9 and remainder 4. " \
                          "It can also be seen that 4, 6, 9 are consecutive terms in a geometric " \
                          "sequence (common ratio 3/2). We will call such numbers, , " \
                          "progressive. Some progressive numbers, such as 9 and 10404 = 102 , " \
                          "happen to also be perfect squares. The sum of all progressive perfect " \
                          "squares below one hundred thousand is 124657. Find the sum of all " \
                          "progressive perfect squares below one trillion (10 )."

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

