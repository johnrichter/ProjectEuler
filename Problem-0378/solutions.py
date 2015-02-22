
__problem_title__ = "Triangle Triples"
__problem_url___ = "https://projecteuler.net/problem=378"
__problem_description__ = "Let dT( ) be the number of divisors of T( ). E.g.: T(7) = 28 and " \
                          "dT(7) = 6. Let Tr( ) be the number of triples ( , , ) such that 1 ≤ " \
                          "Find Tr(60 000 000). Give the last 18 digits of your answer."

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

