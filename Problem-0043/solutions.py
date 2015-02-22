
__problem_title__ = "Sub-string divisibility"
__problem_url___ = "https://projecteuler.net/problem=43"
__problem_description__ = "The number, 1406357289, is a 0 to 9 pandigital number because it is " \
                          "made up of each of the digits 0 to 9 in some order, but it also has a " \
                          "rather interesting sub-string divisibility property. Let be the 1 " \
                          "digit, be the 2 digit, and so on. In this way, we note the following: " \
                          "Find the sum of all 0 to 9 pandigital numbers with this property."

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

