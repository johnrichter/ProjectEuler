
__problem_title__ = "Prime power triples"
__problem_url___ = "https://projecteuler.net/problem=87"
__problem_description__ = "The smallest number expressible as the sum of a prime square, prime " \
                          "cube, and prime fourth power is 28. In fact, there are exactly four " \
                          "numbers below fifty that can be expressed in such a way: 28 = 2 + 2 + " \
                          "2 33 = 3 + 2 + 2 49 = 5 + 2 + 2 47 = 2 + 3 + 2 How many numbers below " \
                          "fifty million can be expressed as the sum of a prime square, prime " \
                          "cube, and prime fourth power?"

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

