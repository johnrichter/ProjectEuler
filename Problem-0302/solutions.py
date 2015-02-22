
__problem_title__ = "Strong Achilles Numbers"
__problem_url___ = "https://projecteuler.net/problem=302"
__problem_description__ = "A positive integer is if p is a divisor of for every prime factor p " \
                          "in . A positive integer is a if can be expressed as a power of " \
                          "another positive integer. A positive integer is an if is powerful but " \
                          "not a perfect power. For example, 864 and 1800 are Achilles numbers: " \
                          "864 = 2 ·3 and 1800 = 2 ·3 ·5 . We shall call a positive integer a if " \
                          "both and φ( ) are Achilles numbers. For example, 864 is a Strong " \
                          "Achilles number: φ(864) = 288 = 2 ·3 . However, 1800 isn't a Strong " \
                          "Achilles number because: φ(1800) = 480 = 2 ·3 ·5 . There are 7 Strong " \
                          "Achilles numbers below 10 and 656 below 10 . How many Strong Achilles " \
                          "numbers are there below 10 ? φ denotes ."

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

