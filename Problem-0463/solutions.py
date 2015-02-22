
__problem_title__ = "A weird recurrence relation"
__problem_url___ = "https://projecteuler.net/problem=463"
__problem_description__ = "The function $f$ is defined for all positive integers as follows: The " \
                          "function $S(n)$ is defined as $\sum_{i=1}^{n}f(i)$. $S(8)=22$ and " \
                          "$S(100)=3604$. Find $S(3^{37})$. Give the last 9 digits of your " \
                          "answer."

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

