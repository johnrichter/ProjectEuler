
__problem_title__ = "A huge binomial coefficient"
__problem_url___ = "https://projecteuler.net/problem=365"
__problem_description__ = "The binomial coeffient C(10 ,10 ) is a number with more than 9 " \
                          "billion (9×10 ) digits. Let M(n,k,m) denote the binomial coefficient " \
                          "C(n,k) modulo m. Calculate ∑M(10 ,10 ,p*q*r) for 1000<p<q<r<5000 and " \
                          "p,q,r prime."

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

