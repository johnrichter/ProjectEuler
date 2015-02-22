
__problem_title__ = "The prime factorisation of binomial coefficients"
__problem_url___ = "https://projecteuler.net/problem=231"
__problem_description__ = "The binomial coefficient C = 120. 120 = 2 × 3 × 5 = 2 × 2 × 2 × 3 × " \
                          "5, and 2 + 2 + 2 + 3 + 5 = 14. So the sum of the terms in the prime " \
                          "factorisation of C is 14. Find the sum of the terms in the prime " \
                          "factorisation of C ."

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

