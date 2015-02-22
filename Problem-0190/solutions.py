
__problem_title__ = "Maximising a weighted product"
__problem_url___ = "https://projecteuler.net/problem=190"
__problem_description__ = "Let S = (x , x , ... , x ) be the m-tuple of positive real numbers " \
                          "with x + x + ... + x = m for which P = x * x * ... * x is maximised. " \
                          "For example, it can be verified that [P ] = 4112 ([ ] is the integer " \
                          "part function). Find Σ[P ] for 2 ≤ m ≤ 15."

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

