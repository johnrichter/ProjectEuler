
__problem_title__ = "Tribonacci non-divisors"
__problem_url___ = "https://projecteuler.net/problem=225"
__problem_description__ = "The sequence 1, 1, 1, 3, 5, 9, 17, 31, 57, 105, 193, 355, 653, 1201 " \
                          "... is defined by T = T = T = 1 and T = T + T + T . It can be shown " \
                          "that 27 does not divide any terms of this sequence. In fact, 27 is " \
                          "the first odd number with this property. Find the 124 odd number that " \
                          "does not divide any terms of the above sequence."

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

