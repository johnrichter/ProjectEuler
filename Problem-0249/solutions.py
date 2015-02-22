
__problem_title__ = "Prime Subset Sums"
__problem_url___ = "https://projecteuler.net/problem=249"
__problem_description__ = "Let = {2, 3, 5, ..., 4999} be the set of prime numbers less than " \
                          "5000. Find the number of subsets of , the sum of whose elements is a " \
                          "prime number. Enter the rightmost 16 digits as your answer."

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

