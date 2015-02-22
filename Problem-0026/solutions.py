
__problem_title__ = "Reciprocal cycles"
__problem_url___ = "https://projecteuler.net/problem=26"
__problem_description__ = "A unit fraction contains 1 in the numerator. The decimal " \
                          "representation of the unit fractions with denominators 2 to 10 are " \
                          "given: Where 0.1(6) means 0.166666..., and has a 1-digit recurring " \
                          "cycle. It can be seen that / has a 6-digit recurring cycle. Find the " \
                          "value of < 1000 for which / contains the longest recurring cycle in " \
                          "its decimal fraction part."

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

