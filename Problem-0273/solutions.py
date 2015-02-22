
__problem_title__ = "Sum of Squares"
__problem_url___ = "https://projecteuler.net/problem=273"
__problem_description__ = "Consider equations of the form: + = , 0 ≤ ≤ , , and integer. For =65 " \
                          "there are two solutions: =1, =8 and =4, =7. We call S( ) the sum of " \
                          "the values of of all solutions of + = , 0 ≤ ≤ , , and integer. Thus " \
                          "S(65) = 1 + 4 = 5. Find ∑S( ), for all squarefree only divisible by " \
                          "primes of the form 4 +1 with 4 +1 < 150."

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

