
__problem_title__ = "Number letter counts"
__problem_url___ = "https://projecteuler.net/problem=17"
__problem_description__ = "If the numbers 1 to 5 are written out in words: one, two, three, " \
                          "four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in " \
                          "total. If all the numbers from 1 to 1000 (one thousand) inclusive " \
                          "were written out in words, how many letters would be used? Do not " \
                          "count spaces or hyphens. For example, 342 (three hundred and " \
                          "forty-two) contains 23 letters and 115 (one hundred and fifteen) " \
                          "contains 20 letters. The use of "and" when writing out numbers is in " \
                          "compliance with British usage."

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

