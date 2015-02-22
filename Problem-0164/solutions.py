
__problem_title__ = "Numbers for which no three consecutive digits have a sum greater than a given value"
__problem_url___ = "https://projecteuler.net/problem=164"
__problem_description__ = "How many 20 digit numbers (without any leading zero) exist such that " \
                          "no three consecutive digits of have a sum greater than 9?"

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

