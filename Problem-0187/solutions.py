
__problem_title__ = "Semiprimes"
__problem_url___ = "https://projecteuler.net/problem=187"
__problem_description__ = "A composite is a number containing at least two prime factors. For " \
                          "example, 15 = 3 × 5; 9 = 3 × 3; 12 = 2 × 2 × 3. There are ten " \
                          "composites below thirty containing precisely two, not necessarily " \
                          "distinct, prime factors: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26. How " \
                          "many composite integers, < 10 , have precisely two, not necessarily " \
                          "distinct, prime factors?"

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

