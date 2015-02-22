
__problem_title__ = "Binary Circles"
__problem_url___ = "https://projecteuler.net/problem=265"
__problem_description__ = "2 binary digits can be placed in a circle so that all the N-digit " \
                          "clockwise subsequences are distinct. For N=3, two such circular " \
                          "arrangements are possible, ignoring rotations: For the first " \
                          "arrangement, the 3-digit subsequences, in clockwise order, are: 000, " \
                          "001, 010, 101, 011, 111, 110 and 100. Each circular arrangement can " \
                          "be encoded as a number by concatenating the binary digits starting " \
                          "with the subsequence of all zeros as the most significant bits and " \
                          "proceeding clockwise. The two arrangements for N=3 are thus " \
                          "represented as 23 and 29: Calling S(N) the sum of the unique numeric " \
                          "representations, we can see that S(3) = 23 + 29 = 52. Find S(5)."

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

