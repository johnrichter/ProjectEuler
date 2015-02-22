
__problem_title__ = "The hyperexponentiation of a number"
__problem_url___ = "https://projecteuler.net/problem=188"
__problem_description__ = "The or of a number a by a positive integer b, denoted by a↑↑b or a, " \
                          "is recursively defined by: a↑↑1 = a, a↑↑(k+1) = a . Thus we have e.g. " \
                          "3↑↑2 = 3 = 27, hence 3↑↑3 = 3 = 7625597484987 and 3↑↑4 is roughly 10 " \
                          ". Find the last 8 digits of 1777↑↑1855."

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

