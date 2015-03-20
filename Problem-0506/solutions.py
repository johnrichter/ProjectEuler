
__problem_title__ = "Clock sequence"
__problem_url___ = "https://projecteuler.net/problem=506"
__problem_description__ = "Consider the infinite repeating sequence of digits: " \
                          "1234321234321234321... Amazingly, you can break this sequence of " \
                          "digits into a sequence of integers such that the sum of the digits in " \
                          "the 'th value is . The sequence goes as follows: 1, 2, 3, 4, 32, 123, " \
                          "43, 2123, 432, 1234, 32123, ... Let be the 'th value in this " \
                          "sequence. For example, = 2, = 32 and = 32123. Let ( ) be + + ... + . " \
                          "For example, (11) = 36120, and (1000) mod 123454321 = 18232686. Find " \
                          "(10 ) mod 123454321."

import timeit


class Solution():

    @staticmethod
    def solution1():
        pass

    @staticmethod
    def time_solutions(runs):
        setup = 'from __main__ import Solution'
        print('Solution 1:', timeit.timeit('Solution.solution1()', setup=setup, number=runs))


if __name__ == '__main__':
    s = Solution()
    print(s.solution1())
    s.time_solutions(1)

