
__problem_title__ = "Odd period square roots"
__problem_url___ = "https://projecteuler.net/problem=64"
__problem_description__ = "All square roots are periodic when written as continued fractions and " \
                          "can be written in the form: For example, let us consider √23: If we " \
                          "continue we would get the following expansion: The process can be " \
                          "summarised as follows: It can be seen that the sequence is repeating. " \
                          "For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate " \
                          "that the block (1,3,1,8) repeats indefinitely. The first ten " \
                          "continued fraction representations of (irrational) square roots are: " \
                          "√2=[1;(2)], period=1 √3=[1;(1,2)], period=2 √5=[2;(4)], period=1 " \
                          "√6=[2;(2,4)], period=2 √7=[2;(1,1,1,4)], period=4 √8=[2;(1,4)], " \
                          "period=2 √10=[3;(6)], period=1 √11=[3;(3,6)], period=2 √12= " \
                          "[3;(2,6)], period=2 √13=[3;(1,1,1,1,6)], period=5 Exactly four " \
                          "continued fractions, for ≤ 13, have an odd period. How many continued " \
                          "fractions for ≤ 10000 have an odd period?"

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

