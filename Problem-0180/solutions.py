
__problem_title__ = "Rational zeros of a function of three variables"
__problem_url___ = "https://projecteuler.net/problem=180"
__problem_description__ = "For any integer , consider the three functions ( , , ) = + − ( , , ) " \
                          "= ( + + )*( + − ) ( , , ) = *( + − ) and their combination ( , , ) = " \
                          "( , , ) + ( , , ) − ( , , ) We call ( , , ) a golden triple of order " \
                          "if , , and are all rational numbers of the form / with 0 < < ≤ and " \
                          "there is (at least) one integer , so that ( , , ) = 0. Let ( , , ) = " \
                          "+ + . Let = / be the sum of all distinct ( , , ) for all golden " \
                          "triples ( , , ) of order 35. All the ( , , ) and must be in reduced " \
                          "form. Find + ."

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

