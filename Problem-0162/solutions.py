
__problem_title__ = "Hexadecimal numbers"
__problem_url___ = "https://projecteuler.net/problem=162"
__problem_description__ = "In the hexadecimal number system numbers are represented using 16 " \
                          "different digits: The hexadecimal number AF when written in the " \
                          "decimal number system equals 10x16+15=175. In the 3-digit hexadecimal " \
                          "numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present. " \
                          "Like numbers written in base ten we write hexadecimal numbers without " \
                          "leading zeroes. How many hexadecimal numbers containing at most " \
                          "sixteen hexadecimal digits exist with all of the digits 0,1, and A " \
                          "present at least once? Give your answer as a hexadecimal number. " \
                          "(A,B,C,D,E and F in upper case, without any leading or trailing code " \
                          "that marks the number as hexadecimal and without leading zeroes , " \
                          "e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F " \
                          "and not 0000001A3F)"

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

