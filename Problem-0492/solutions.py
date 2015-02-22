
__problem_title__ = "Exploding sequence"
__problem_url___ = "https://projecteuler.net/problem=492"
__problem_description__ = "Define the sequence a , a , a , ... as: Examples: a = 2359 a = " \
                          "269221280981320216750489044576319 a mod 1 000 000 007 = 203064689 a " \
                          "mod 1 000 000 007 = 456482974 Define B( , , ) as ∑ (a mod ) for every " \
                          "prime such that ≤ ≤ + . Examples: B(10 , 10 , 10 ) = 23674718882 B(10 " \
                          ", 10 , 10 ) = 20731563854 Find B(10 , 10 , 10 )."

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

