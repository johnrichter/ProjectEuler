
__problem_title__ = "Golomb's self-describing sequence"
__problem_url___ = "https://projecteuler.net/problem=341"
__problem_description__ = "The {G( )} is the only nondecreasing sequence of natural numbers such " \
                          "that appears exactly G( ) times in the sequence. The values of G( ) " \
                          "for the first few are You are given that G(10 ) = 86, G(10 ) = 6137. " \
                          "You are also given that ΣG( ) = 153506976 for 1 ≤ < 10 . Find ΣG( ) " \
                          "for 1 ≤ < 10 ."

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

