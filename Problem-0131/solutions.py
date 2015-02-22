
__problem_title__ = "Prime cube partnership"
__problem_url___ = "https://projecteuler.net/problem=131"
__problem_description__ = "There are some prime values, , for which there exists a positive " \
                          "integer, , such that the expression + is a perfect cube. For example, " \
                          "when = 19, 8 + 8 ×19 = 12 . What is perhaps most surprising is that " \
                          "for each prime with this property the value of is unique, and there " \
                          "are only four such primes below one-hundred. How many primes below " \
                          "one million have this remarkable property?"

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

