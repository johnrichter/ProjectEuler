
__problem_title__ = "Linear Combinations of Semiprimes"
__problem_url___ = "https://projecteuler.net/problem=278"
__problem_description__ = "Given the values of integers 1 < < <... < , consider the linear " \
                          "combination + + ... + = , using only integer values ≥ 0. Note that " \
                          "for a given set of , it may be that not all values of are possible. " \
                          "For instance, if = 5 and = 7, there are no ≥ 0 and ≥ 0 such that " \
                          "could be 1, 2, 3, 4, 6, 8, 9, 11, 13, 16, 18 or 23. In fact, 23 is " \
                          "the largest impossible value of for = 5 and = 7. We therefore call " \
                          "(5, 7) = 23. Similarly, it can be shown that (6, 10, 15)=29 and (14, " \
                          "22, 77) = 195. Find ∑ ( ), where , and are prime numbers and &lt < < " \
                          "5000."

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

