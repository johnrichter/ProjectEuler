
__problem_title__ = "Digit cancelling fractions"
__problem_url___ = "https://projecteuler.net/problem=33"
__problem_description__ = "The fraction / is a curious fraction, as an inexperienced " \
                          "mathematician in attempting to simplify it may incorrectly believe " \
                          "that / = / , which is correct, is obtained by cancelling the 9s. We " \
                          "shall consider fractions like, / = / , to be trivial examples. There " \
                          "are exactly four non-trivial examples of this type of fraction, less " \
                          "than one in value, and containing two digits in the numerator and " \
                          "denominator. If the product of these four fractions is given in its " \
                          "lowest common terms, find the value of the denominator."

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

