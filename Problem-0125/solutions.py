
__problem_title__ = "Palindromic sums"
__problem_url___ = "https://projecteuler.net/problem=125"
__problem_description__ = "The palindromic number 595 is interesting because it can be written " \
                          "as the sum of consecutive squares: 6 + 7 + 8 + 9 + 10 + 11 + 12 . " \
                          "There are exactly eleven palindromes below one-thousand that can be " \
                          "written as consecutive square sums, and the sum of these palindromes " \
                          "is 4164. Note that 1 = 0 + 1 has not been included as this problem is " \
                          "concerned with the squares of positive integers. Find the sum of all " \
                          "the numbers less than 10 that are both palindromic and can be written " \
                          "as the sum of consecutive squares."

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

