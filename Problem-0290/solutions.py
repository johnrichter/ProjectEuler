
__problem_title__ = "Digital Signature"
__problem_url___ = "https://projecteuler.net/problem=290"
__problem_description__ = "How many integers 0 ≤ &lt 10 have the property that the sum of the " \
                          "digits of equals the sum of digits of 137 ?"

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

