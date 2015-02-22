
__problem_title__ = "Maximal coprime subset"
__problem_url___ = "https://projecteuler.net/problem=355"
__problem_description__ = "Define Co( ) to be the maximal possible sum of a set of mutually " \
                          "co-prime elements from {1, 2, ..., }. For example Co(10) is 30 and " \
                          "hits that maximum on the subset {1, 5, 7, 8, 9}. You are given that " \
                          "Co(30) = 193 and Co(100) = 1356. Find Co(200000)."

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

