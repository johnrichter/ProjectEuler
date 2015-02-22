
__problem_title__ = "Top Dice"
__problem_url___ = "https://projecteuler.net/problem=240"
__problem_description__ = "There are 1111 ways in which five 6-sided dice (sides numbered 1 to " \
                          "6) can be rolled so that the top three sum to 15. Some examples are: " \
                          "D ,D ,D ,D ,D = 4,3,6,3,5 D ,D ,D ,D ,D = 4,3,3,5,6 D ,D ,D ,D ,D = " \
                          "3,3,3,6,6 D ,D ,D ,D ,D = 6,6,3,3,3 In how many ways can twenty " \
                          "12-sided dice (sides numbered 1 to 12) be rolled so that the top ten " \
                          "sum to 70?"

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

