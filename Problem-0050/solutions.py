
__problem_title__ = "Consecutive prime sum"
__problem_url___ = "https://projecteuler.net/problem=50"
__problem_description__ = "The prime 41, can be written as the sum of six consecutive primes: " \
                          "This is the longest sum of consecutive primes that adds to a prime " \
                          "below one-hundred. The longest sum of consecutive primes below " \
                          "one-thousand that adds to a prime, contains 21 terms, and is equal to " \
                          "953. Which prime, below one-million, can be written as the sum of the " \
                          "most consecutive primes?"

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

