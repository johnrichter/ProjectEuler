
__problem_title__ = "Prime connection"
__problem_url___ = "https://projecteuler.net/problem=425"
__problem_description__ = "Two positive numbers A and B are said to be (denoted by "A ↔ B") if " \
                          "one of these conditions holds: (1) A and B have the same length and " \
                          "differ in exactly one digit; for example, 123 ↔ 173. (2) Adding one " \
                          "digit to the left of A (or B) makes B (or A); for example, 23 ↔ 223 " \
                          "and 123 ↔ 23. We call a prime P a if there exists a chain of " \
                          "connected primes between 2 and P and no prime in the chain exceeds P. " \
                          "For example, 127 is a 2's relative. One of the possible chains is " \
                          "shown below: 2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127 However, 11 and 103 " \
                          "are not 2's relatives. Let F(N) be the sum of the primes ≤ N which " \
                          "are not 2's relatives. We can verify that F(10 ) = 431 and F(10 ) = " \
                          "78728. Find F(10 )."

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

