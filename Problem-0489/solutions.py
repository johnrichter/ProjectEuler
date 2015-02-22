
__problem_title__ = "Common factors between two sequences"
__problem_url___ = "https://projecteuler.net/problem=489"
__problem_description__ = "Let ( , ) be the smallest non-negative integer for which ( + , ( + ) " \
                          "+ ) is maximized. For example, (1, 1) = 5 because gcd( + 1, ( + 1) + " \
                          "1) reaches its maximum value of 7 for = 5, and is smaller for 0 ≤ n < " \
                          "5. Let ( , ) = Σ ( , ) for 1 ≤ ≤ , 1 ≤ ≤ . You are given (5, 5) = " \
                          "128878 and (10, 10) = 32936544. Find (18, 1900)."

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

