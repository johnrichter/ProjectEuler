
__problem_title__ = "Longest Collatz sequence"
__problem_url___ = "https://projecteuler.net/problem=14"
__problem_description__ = "The following iterative sequence is defined for the set of positive " \
                          "integers: → /2 ( is even) → 3 + 1 ( is odd) Using the rule above and " \
                          "starting with 13, we generate the following sequence: It can be seen " \
                          "that this sequence (starting at 13 and finishing at 1) contains 10 " \
                          "terms. Although it has not been proved yet (Collatz Problem), it is " \
                          "thought that all starting numbers finish at 1. Which starting number, " \
                          "under one million, produces the longest chain? Once the chain starts " \
                          "the terms are allowed to go above one million."

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

