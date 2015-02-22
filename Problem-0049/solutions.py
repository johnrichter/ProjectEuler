
__problem_title__ = "Prime permutations"
__problem_url___ = "https://projecteuler.net/problem=49"
__problem_description__ = "The arithmetic sequence, 1487, 4817, 8147, in which each of the terms " \
                          "increases by 3330, is unusual in two ways: (i) each of the three " \
                          "terms are prime, and, (ii) each of the 4-digit numbers are " \
                          "permutations of one another. There are no arithmetic sequences made " \
                          "up of three 1-, 2-, or 3-digit primes, exhibiting this property, but " \
                          "there is one other 4-digit increasing sequence. What 12-digit number " \
                          "do you form by concatenating the three terms in this sequence?"

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

