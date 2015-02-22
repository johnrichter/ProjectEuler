
__problem_title__ = "Diophantine equation"
__problem_url___ = "https://projecteuler.net/problem=66"
__problem_description__ = "Consider quadratic Diophantine equations of the form: – D = 1 For " \
                          "example, when D=13, the minimal solution in is 649 – 13×180 = 1. It " \
                          "can be assumed that there are no solutions in positive integers when " \
                          "D is square. By finding minimal solutions in for D = {2, 3, 5, 6, 7}, " \
                          "we obtain the following: 3 – 2×2 = 1 2 – 3×1 = 1 – 5×4 = 1 5 – 6×2 = " \
                          "1 8 – 7×3 = 1 Hence, by considering minimal solutions in for D ≤ 7, " \
                          "the largest is obtained when D=5. Find the value of D ≤ 1000 in " \
                          "minimal solutions of for which the largest value of is obtained."

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

