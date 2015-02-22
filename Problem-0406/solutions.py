
__problem_title__ = "Guessing Game"
__problem_url___ = "https://projecteuler.net/problem=406"
__problem_description__ = "We are trying to find a hidden number selected from the set of " \
                          "integers {1, 2, ..., } by asking questions. Each number (question) we " \
                          "ask, we get one of three possible answers: Given the value of , , and " \
                          ", an minimizes the total cost . For example, if = 5, = 2, and = 3, " \
                          "then we may begin by asking " " as our first question. If we are told " \
                          "that 2 is higher than the hidden number (for a cost of =3), then we " \
                          "are sure that " " is the hidden number (for a total cost of ). If we " \
                          "are told that 2 is lower than the hidden number (for a cost of =2), " \
                          "then our next question will be " ". If we are told that 4 is higher " \
                          "than the hidden number (for a cost of =3), then we are sure that " " " \
                          "is the hidden number (for a total cost of 2+3= ). If we are told that " \
                          "4 is lower than the hidden number (for a cost of =2), then we are " \
                          "sure that " " is the hidden number (for a total cost of 2+2= ). Thus, " \
                          "the worst-case cost achieved by this strategy is . It can also be " \
                          "shown that this is the lowest worst-case cost that can be achieved. " \
                          "So, in fact, we have just described an optimal strategy for the given " \
                          "values of , , and . Let C( , , ) be the worst-case cost achieved by " \
                          "an optimal strategy for the given values of , , and . Here are a few " \
                          "examples: C(5, 2, 3) = 5 C(500, √2, √3) = 13.22073197... C(20000, 5, " \
                          "7) = 82 C(2000000, √5, √7) = 49.63755955... Let F be the Fibonacci " \
                          "numbers: F = F + F with base cases F = F = 1. Find ∑ C(10 , √ , √F ), " \
                          "and give your answer rounded to 8 decimal places behind the decimal " \
                          "point."

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

