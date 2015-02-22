
__problem_title__ = "Counting summations"
__problem_url___ = "https://projecteuler.net/problem=76"
__problem_description__ = "It is possible to write five as a sum in exactly six different ways: " \
                          "4 + 1 3 + 2 3 + 1 + 1 2 + 2 + 1 2 + 1 + 1 + 1 1 + 1 + 1 + 1 + 1 How " \
                          "many different ways can one hundred be written as a sum of at least " \
                          "two positive integers?"

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

