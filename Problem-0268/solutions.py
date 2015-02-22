
__problem_title__ = "Counting numbers with at least four distinct prime factors less than 100"
__problem_url___ = "https://projecteuler.net/problem=268"
__problem_description__ = "It can be verified that there are 23 positive integers less than 1000 " \
                          "that are divisible by at least four distinct primes less than 100. " \
                          "Find how many positive integers less than 10 are divisible by at " \
                          "least four distinct primes less than 100."

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

