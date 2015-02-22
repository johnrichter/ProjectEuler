
__problem_title__ = "Reciprocal cycles II"
__problem_url___ = "https://projecteuler.net/problem=417"
__problem_description__ = "A unit fraction contains 1 in the numerator. The decimal " \
                          "representation of the unit fractions with denominators 2 to 10 are " \
                          "given: Where 0.1(6) means 0.166666..., and has a 1-digit recurring " \
                          "cycle. It can be seen that / has a 6-digit recurring cycle. Unit " \
                          "fractions whose denominator has no other prime factors than 2 and/or " \
                          "5 are not considered to have a recurring cycle. We define the length " \
                          "of the recurring cycle of those unit fractions as 0. Let L(n) denote " \
                          "the length of the recurring cycle of 1/n. You are given that ∑L(n) " \
                          "for 3 ≤ n ≤ 1 000 000 equals 55535191115. Find ∑L(n) for 3 ≤ n ≤ 100 " \
                          "000 000"

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

