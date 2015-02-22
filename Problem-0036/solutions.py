
__problem_title__ = "Double-base palindromes"
__problem_url___ = "https://projecteuler.net/problem=36"
__problem_description__ = "The decimal number, 585 = 1001001001 (binary), is palindromic in both " \
                          "bases. Find the sum of all numbers, less than one million, which are " \
                          "palindromic in base 10 and base 2. (Please note that the palindromic " \
                          "number, in either base, may not include leading zeros.)"

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

