
__problem_title__ = "Chip Defects"
__problem_url___ = "https://projecteuler.net/problem=307"
__problem_description__ = "defects are randomly distributed amongst integrated-circuit chips " \
                          "produced by a factory (any number of defects may be found on a chip " \
                          "and each defect is independent of the other defects). Let p( ) " \
                          "represent the probability that there is a chip with at least 3 " \
                          "defects. For instance p(3,7) ≈ 0.0204081633. Find p(20 000, 1 000 " \
                          "000) and give your answer rounded to 10 decimal places in the form " \
                          "0.abcdefghij"

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

