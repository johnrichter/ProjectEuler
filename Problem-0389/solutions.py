
__problem_title__ = "Platonic Dice"
__problem_url___ = "https://projecteuler.net/problem=389"
__problem_description__ = "An unbiased single 4-sided die is thrown and its value, , is noted. " \
                          "unbiased 6-sided dice are thrown and their scores are added together. " \
                          "The sum, , is noted. unbiased 8-sided dice are thrown and their " \
                          "scores are added together. The sum, , is noted. unbiased 12-sided " \
                          "dice are thrown and their scores are added together. The sum, , is " \
                          "noted. unbiased 20-sided dice are thrown and their scores are added " \
                          "together. The sum, , is noted. Find the variance of , and give your " \
                          "answer rounded to 4 decimal places."

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

