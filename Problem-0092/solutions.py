
__problem_title__ = "Square digit chains"
__problem_url___ = "https://projecteuler.net/problem=92"
__problem_description__ = "A number chain is created by continuously adding the square of the " \
                          "digits in a number to form a new number until it has been seen " \
                          "before. For example, 44 → 32 → 13 → 10 → → 85 → → 145 → 42 → 20 → 4 → " \
                          "16 → 37 → 58 → Therefore any chain that arrives at 1 or 89 will " \
                          "become stuck in an endless loop. What is most amazing is that EVERY " \
                          "starting number will eventually arrive at 1 or 89. How many starting " \
                          "numbers below ten million will arrive at 89?"

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

