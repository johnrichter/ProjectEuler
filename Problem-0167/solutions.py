
__problem_title__ = "Investigating Ulam sequences"
__problem_url___ = "https://projecteuler.net/problem=167"
__problem_description__ = "For two positive integers a and b, the Ulam sequence U(a,b) is " \
                          "defined by U(a,b) = a, U(a,b) = b and for k > 2, U(a,b) is the " \
                          "smallest integer greater than U(a,b) which can be written in exactly " \
                          "one way as the sum of two distinct previous members of U(a,b). For " \
                          "example, the sequence U(1,2) begins with 1, 2, 3 = 1 + 2, 4 = 1 + 3, " \
                          "6 = 2 + 4, 8 = 2 + 6, 11 = 3 + 8; 5 does not belong to it because 5 = " \
                          "1 + 4 = 2 + 3 has two representations as the sum of two previous " \
                          "members, likewise 7 = 1 + 6 = 3 + 4. Find ∑U(2,2 +1) for 2 ≤ ≤10, " \
                          "where = 10 ."

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

