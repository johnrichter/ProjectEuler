
__problem_title__ = "Distinct primes factors"
__problem_url___ = "https://projecteuler.net/problem=47"
__problem_description__ = "The first two consecutive numbers to have two distinct prime factors " \
                          "are: 14 = 2 × 7 15 = 3 × 5 The first three consecutive numbers to " \
                          "have three distinct prime factors are: 644 = 2² × 7 × 23 645 = 3 × 5 " \
                          "× 43 646 = 2 × 17 × 19. Find the first four consecutive integers to " \
                          "have four distinct prime factors. What is the first of these numbers?"

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

