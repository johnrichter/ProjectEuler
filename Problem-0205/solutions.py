
__problem_title__ = "Dice Game"
__problem_url___ = "https://projecteuler.net/problem=205"
__problem_description__ = "Peter has nine four-sided (pyramidal) dice, each with faces numbered " \
                          "1, 2, 3, 4. Colin has six six-sided (cubic) dice, each with faces " \
                          "numbered 1, 2, 3, 4, 5, 6. Peter and Colin roll their dice and " \
                          "compare totals: the highest total wins. The result is a draw if the " \
                          "totals are equal. What is the probability that Pyramidal Pete beats " \
                          "Cubic Colin? Give your answer rounded to seven decimal places in the " \
                          "form 0.abcdefg"

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

