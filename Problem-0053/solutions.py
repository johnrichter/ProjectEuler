
__problem_title__ = "Combinatoric selections"
__problem_url___ = "https://projecteuler.net/problem=53"
__problem_description__ = "There are exactly ten ways of selecting three from five, 12345: 123, " \
                          "124, 125, 134, 135, 145, 234, 235, 245, and 345 In combinatorics, we " \
                          "use the notation, C = 10. In general, It is not until = 23, that a " \
                          "value exceeds one-million: C = 1144066. How many, not necessarily " \
                          "distinct, values of C , for 1 ≤ ≤ 100, are greater than one-million?"

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

