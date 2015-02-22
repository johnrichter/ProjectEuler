
__problem_title__ = "Pythagorean odds"
__problem_url___ = "https://projecteuler.net/problem=285"
__problem_description__ = "Albert chooses a positive integer , then two real numbers , are " \
                          "randomly chosen in the interval [0,1] with uniform distribution. The " \
                          "square root of the sum ( · +1) + ( · +1) is then computed and rounded " \
                          "to the nearest integer. If the result is equal to , he scores points; " \
                          "otherwise he scores nothing. For example, if = 6, = 0.2 and = 0.85, " \
                          "then ( · +1) + ( · +1) = 42.05. The square root of 42.05 is 6.484... " \
                          "and when rounded to the nearest integer, it becomes 6. This is equal " \
                          "to , so he scores 6 points. It can be shown that if he plays 10 turns " \
                          "with = 1, = 2, ..., = 10, the expected value of his total score, " \
                          "rounded to five decimal places, is 10.20914. If he plays 10 turns " \
                          "with = 1, = 2, = 3, ..., = 10 , what is the expected value of his " \
                          "total score, rounded to five decimal places?"

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

