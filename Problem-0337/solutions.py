
__problem_title__ = "Totient Stairstep Sequences"
__problem_url___ = "https://projecteuler.net/problem=337"
__problem_description__ = "Let {a , a ,..., a } be an integer sequence of length such that: Let " \
                          "S( ) be the number of such sequences with a ≤ . For example, S(10) = " \
                          "4: {6}, {6, 8}, {6, 8, 9} and {6, 10}. We can verify that S(100) = " \
                          "482073668 and S(10 000) mod 10 = 73808307. Find S(20 000 000) mod 10 " \
                          ". φ denotes ."

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

