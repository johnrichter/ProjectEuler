
__problem_title__ = "Investigating a Prime Pattern "
__problem_url___ = "https://projecteuler.net/problem=146"
__problem_description__ = "The smallest positive integer for which the numbers +1, +3, +7, +9, " \
                          "+13, and +27 are consecutive primes is 10. The sum of all such " \
                          "integers below one-million is 1242490. What is the sum of all such " \
                          "integers below 150 million?"

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

