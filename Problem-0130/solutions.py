
__problem_title__ = "Composites with prime repunit property"
__problem_url___ = "https://projecteuler.net/problem=130"
__problem_description__ = "A number consisting entirely of ones is called a repunit. We shall " \
                          "define R( ) to be a repunit of length ; for example, R(6) = 111111. " \
                          "Given that is a positive integer and GCD( , 10) = 1, it can be shown " \
                          "that there always exists a value, , for which R( ) is divisible by , " \
                          "and let A( ) be the least such value of ; for example, A(7) = 6 and " \
                          "A(41) = 5. You are given that for all primes, > 5, that − 1 is " \
                          "divisible by A( ). For example, when = 41, A(41) = 5, and 40 is " \
                          "divisible by 5. However, there are rare composite values for which " \
                          "this is also true; the first five examples being 91, 259, 451, 481, " \
                          "and 703. Find the sum of the first twenty-five composite values of " \
                          "for which GCD( , 10) = 1 and − 1 is divisible by A( )."

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

