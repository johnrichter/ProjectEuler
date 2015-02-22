
__problem_title__ = "Squarefree Binomial Coefficients"
__problem_url___ = "https://projecteuler.net/problem=203"
__problem_description__ = "The binomial coefficients C can be arranged in triangular form, " \
                          "Pascal's triangle, like this: It can be seen that the first eight " \
                          "rows of Pascal's triangle contain twelve distinct numbers: 1, 2, 3, " \
                          "4, 5, 6, 7, 10, 15, 20, 21 and 35. A positive integer is called " \
                          "squarefree if no square of a prime divides . Of the twelve distinct " \
                          "numbers in the first eight rows of Pascal's triangle, all except 4 " \
                          "and 20 are squarefree. The sum of the distinct squarefree numbers in " \
                          "the first eight rows is 105. Find the sum of the distinct squarefree " \
                          "numbers in the first 51 rows of Pascal's triangle."

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

