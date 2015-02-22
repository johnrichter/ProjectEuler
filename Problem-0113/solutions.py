
__problem_title__ = "Non-bouncy numbers"
__problem_url___ = "https://projecteuler.net/problem=113"
__problem_description__ = "Working from left-to-right if no digit is exceeded by the digit to " \
                          "its left it is called an increasing number; for example, 134468. " \
                          "Similarly if no digit is exceeded by the digit to its right it is " \
                          "called a decreasing number; for example, 66420. We shall call a " \
                          "positive integer that is neither increasing nor decreasing a "bouncy" " \
                          "number; for example, 155349. As increases, the proportion of bouncy " \
                          "numbers below increases such that there are only 12951 numbers below " \
                          "one-million that are not bouncy and only 277032 non-bouncy numbers " \
                          "below 10 . How many numbers below a googol (10 ) are not bouncy?"

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

