
__problem_title__ = "Arithmetic expressions"
__problem_url___ = "https://projecteuler.net/problem=93"
__problem_description__ = "By using each of the digits from the set, {1, 2, 3, 4}, exactly once, " \
                          "and making use of the four arithmetic operations (+, −, *, /) and " \
                          "brackets/parentheses, it is possible to form different positive " \
                          "integer targets. For example, 8 = (4 * (1 + 3)) / 2 14 = 4 * (3 + 1 / " \
                          "2) 19 = 4 * (2 + 3) − 1 36 = 3 * 4 * (2 + 1) Note that concatenations " \
                          "of the digits, like 12 + 34, are not allowed. Using the set, {1, 2, " \
                          "3, 4}, it is possible to obtain thirty-one different target numbers " \
                          "of which 36 is the maximum, and each of the numbers 1 to 28 can be " \
                          "obtained before encountering the first non-expressible number. Find " \
                          "the set of four distinct digits, < &lt < , for which the longest set " \
                          "of consecutive positive integers, 1 to , can be obtained, giving your " \
                          "answer as a string: ."

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

