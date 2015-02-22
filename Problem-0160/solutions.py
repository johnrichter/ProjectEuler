
__problem_title__ = "Factorial trailing digits"
__problem_url___ = "https://projecteuler.net/problem=160"
__problem_description__ = "For any N, let f(N) be the last five digits before the trailing " \
                          "zeroes in N!. For example, 9! = 362880 so f(9)=36288 10! = 3628800 so " \
                          "f(10)=36288 20! = 2432902008176640000 so f(20)=17664 Find " \
                          "f(1,000,000,000,000)"

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

