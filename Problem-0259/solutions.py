
__problem_title__ = "Reachable Numbers"
__problem_url___ = "https://projecteuler.net/problem=259"
__problem_description__ = "A positive integer will be called if it can result from an arithmetic " \
                          "expression obeying the following rules: For example, 42 is reachable, " \
                          "since (1/23) * ((4*5)-6) * (78-9) = 42. What is the sum of all " \
                          "positive reachable integers?"

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

