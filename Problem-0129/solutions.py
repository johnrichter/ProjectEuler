
__problem_title__ = "Repunit divisibility"
__problem_url___ = "https://projecteuler.net/problem=129"
__problem_description__ = "A number consisting entirely of ones is called a repunit. We shall " \
                          "define R( ) to be a repunit of length ; for example, R(6) = 111111. " \
                          "Given that is a positive integer and GCD( , 10) = 1, it can be shown " \
                          "that there always exists a value, , for which R( ) is divisible by , " \
                          "and let A( ) be the least such value of ; for example, A(7) = 6 and " \
                          "A(41) = 5. The least value of for which A( ) first exceeds ten is 17. " \
                          "Find the least value of for which A( ) first exceeds one-million."

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

