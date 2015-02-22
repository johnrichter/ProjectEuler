
__problem_title__ = "Last digits of divisors"
__problem_url___ = "https://projecteuler.net/problem=474"
__problem_description__ = "For a positive integer and digits , we define F( , ) as the number of " \
                          "the divisors of whose last digits equal . For example, F(84, 4) = 3. " \
                          "Among the divisors of 84 (1, 2, 3, 4, 6, 7, 12, 14, 21, 28, 42, 84), " \
                          "three of them (4, 14, 84) have the last digit 4. We can also verify " \
                          "that F(12!, 12) = 11 and F(50!, 123) = 17888. Find F(10 !, 65432) " \
                          "modulo (10 + 61)."

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

