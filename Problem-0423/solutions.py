
__problem_title__ = "Consecutive die throws"
__problem_url___ = "https://projecteuler.net/problem=423"
__problem_description__ = "Let be a positive integer. A 6-sided die is thrown times. Let be the " \
                          "number of pairs of consecutive throws that give the same value. For " \
                          "example, if = 7 and the values of the die throws are (1,1,5,6,6,6,3), " \
                          "then the following pairs of consecutive throws give the same value: ( " \
                          ",5,6,6,6,3) (1,1,5, ,6,3) (1,1,5,6, ,3) Therefore, = 3 for " \
                          "(1,1,5,6,6,6,3). Define C( ) as the number of outcomes of throwing a " \
                          "6-sided die times such that does not exceed π( ). For example, C(3) = " \
                          "216, C(4) = 1290, C(11) = 361912500 and C(24) = 4727547363281250000. " \
                          "Define S( ) as ∑ C( ) for 1 ≤ ≤ . For example, S(50) mod 1 000 000 " \
                          "007 = 832833871. Find S(50 000 000) mod 1 000 000 007. π denotes the " \
                          ", i.e. π( ) is the number of primes ≤ ."

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

