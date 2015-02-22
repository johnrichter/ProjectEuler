
__problem_title__ = "Admissible paths through a grid"
__problem_url___ = "https://projecteuler.net/problem=408"
__problem_description__ = "Let's call a lattice point ( , ) if , and + are all positive perfect " \
                          "squares. For example, (9, 16) is inadmissible, while (0, 4), (3, 1) " \
                          "and (9, 4) are not. Consider a path from point ( , ) to point ( , ) " \
                          "using only unit steps north or east. Let's call such a path if none " \
                          "of its intermediate points are inadmissible. Let P( ) be the number " \
                          "of admissible paths from (0, 0) to ( , ). It can be verified that " \
                          "P(5) = 252, P(16) = 596994440 and P(1000) mod 1 000 000 007 = " \
                          "341920854. Find P(10 000 000) mod 1 000 000 007."

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

