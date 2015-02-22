
__problem_title__ = "Sum of digits - experience #23"
__problem_url___ = "https://projecteuler.net/problem=294"
__problem_description__ = "For a positive integer k, define d(k) as the sum of the digits of k " \
                          "in its usual decimal representation. Thus d(42) = 4+2 = 6. For a " \
                          "positive integer n, define S(n) as the number of positive integers k " \
                          "n with the following properties : Find S(11 ) and give your answer " \
                          "mod 10 ."

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

