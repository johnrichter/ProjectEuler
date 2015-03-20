
__problem_title__ = "Bidirectional Recurrence"
__problem_url___ = "https://projecteuler.net/problem=505"
__problem_description__ = "Let: $\begin{array}{ll} x(0)&=0 \\ x(1)&=1 \\ " \
                          "x(2k)&=(3x(k)+2x(\lfloor \frac k 2 \rfloor)) \text{ mod } 2^{60} " \
                          "\text{ for } k \ge 1 \text {, where } \lfloor \text { } \rfloor \text " \
                          "{ is the floor function} \\ x(2k+1)&=(2x(k)+3x(\lfloor \frac k 2 " \
                          "\rfloor)) \text{ mod } 2^{60} \text{ for } k \ge 1 \\ " \
                          "y_n(k)&=\left\{{\begin{array}{lc} x(k) && \text{if } k \ge n \\ " \
                          "2^{60} - 1 - max(y_n(2k),y_n(2k+1)) && \text{if } k You are given: " \
                          "$\begin{array}{ll} x(2)&=3 \\ x(3)&=2 \\ x(4)&=11 \\ y_4(4)&=11 \\ " \
                          "y_4(3)&=2^{60}-9\\ y_4(2)&=2^{60}-12 \\ y_4(1)&=A(4)=8 \\ " \
                          "A(10)&=2^{60}-34\\ A(10^3)&=101881 \end{array}$"

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

