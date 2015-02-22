
__problem_title__ = "Truncatable primes"
__problem_url___ = "https://projecteuler.net/problem=37"
__problem_description__ = "The number 3797 has an interesting property. Being prime itself, it " \
                          "is possible to continuously remove digits from left to right, and " \
                          "remain prime at each stage: 3797, 797, 97, and 7. Similarly we can " \
                          "work from right to left: 3797, 379, 37, and 3. Find the sum of the " \
                          "only eleven primes that are both truncatable from left to right and " \
                          "right to left. NOTE: 2, 3, 5, and 7 are not considered to be " \
                          "truncatable primes."

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

