
__problem_title__ = "Rudin-Shapiro sequence"
__problem_url___ = "https://projecteuler.net/problem=384"
__problem_description__ = "Define the sequence a(n) as the number of adjacent pairs of ones in " \
                          "the binary expansion of n (possibly overlapping). E.g.: a(5) = a(101 " \
                          ") = 0, a(6) = a(110 ) = 1, a(7) = a(111 ) = 2 Define the sequence " \
                          "b(n) = (-1) . This sequence is called the sequence. Also consider the " \
                          "summatory sequence of b(n): . The first couple of values of these " \
                          "sequences are: The sequence s(n) has the remarkable property that all " \
                          "elements are positive and every positive integer k occurs exactly k " \
                          "times. Define g(t,c), with 1 ≤ c ≤ t, as the index in s(n) for which " \
                          "t occurs for the c'th time in s(n). E.g.: g(3,3) = 6, g(4,2) = 7 and " \
                          "g(54321,12345) = 1220847710. Let F(n) be the fibonacci sequence " \
                          "defined by: F(0)=F(1)=1 and F(n)=F(n-1)+F(n-2) for n>1. Define " \
                          "GF(t)=g(F(t),F(t-1)). Find ΣGF(t) for 2≤t≤45."

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

