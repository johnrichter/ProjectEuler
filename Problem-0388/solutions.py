
__problem_title__ = "Distinct Lines"
__problem_url___ = "https://projecteuler.net/problem=388"
__problem_description__ = "Consider all lattice points (a,b,c) with 0 ≤ a,b,c ≤ N. From the " \
                          "origin O(0,0,0) all lines are drawn to the other lattice points. Let " \
                          "D(N) be the number of such lines. You are given that D(1 000 000) = " \
                          "831909254469114121. Find D(10 ). Give as your answer the first nine " \
                          "digits followed by the last nine digits."

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

