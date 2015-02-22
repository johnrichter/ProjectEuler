
__problem_title__ = "Prime triplets"
__problem_url___ = "https://projecteuler.net/problem=196"
__problem_description__ = "Build a triangle from all positive integers in the following way: 1 4 " \
                          "6 8 9 10 12 14 15 16 18 20 21 22 24 25 26 27 28 30 32 33 34 35 36 38 " \
                          "39 40 42 44 45 46 48 49 50 51 52 54 55 56 57 58 60 62 63 64 65 66 . . " \
                          ". Each positive integer has up to eight neighbours in the triangle. A " \
                          "set of three primes is called a if one of the three primes has the " \
                          "other two as neighbours in the triangle. For example, in the second " \
                          "row, the prime numbers 2 and 3 are elements of some prime triplet. If " \
                          "row 8 is considered, it contains two primes which are elements of " \
                          "some prime triplet, i.e. 29 and 31. If row 9 is considered, it " \
                          "contains only one prime which is an element of some prime triplet: " \
                          "37. Define S( ) as the sum of the primes in row which are elements of " \
                          "any prime triplet. Then S(8)=60 and S(9)=37. You are given that " \
                          "S(10000)=950007619. Find S(5678027) + S(7208785)."

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

