
__problem_title__ = "Primonacci"
__problem_url___ = "https://projecteuler.net/problem=304"
__problem_description__ = "For any positive integer the function next_prime( ) returns the " \
                          "smallest prime p such that p> . The sequence a( ) is defined by: " \
                          "a(1)=next_prime(10 ) and a( )=next_prime(a( -1)) for n>1. The " \
                          "fibonacci sequence f( ) is defined by: f(0)=0, f(1)=1 and f( )=f( " \
                          "-1)+f( -2) for >1. The sequence b( ) is defined as f(a( )). Find ∑b( " \
                          ") for 1≤ ≤100 000. Give your answer mod 1234567891011."

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

