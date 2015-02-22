
__problem_title__ = "Polynomials of Fibonacci numbers"
__problem_url___ = "https://projecteuler.net/problem=435"
__problem_description__ = "The {f , n ≥ 0} are defined recursively as f = f + f with base cases " \
                          "f = 0 and f = 1. Define the polynomials {F , n ≥ 0} as F (x) = ∑f x " \
                          "for 0 ≤ i ≤ n. For example, F (x) = x + x + 2x + 3x + 5x + 8x + 13x , " \
                          "and F (11) = 268357683. Let n = 10 . Find the sum [∑ F (x)] mod " \
                          "1307674368000 (= 15!)."

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

