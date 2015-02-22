
__problem_title__ = "Palindrome-containing strings"
__problem_url___ = "https://projecteuler.net/problem=486"
__problem_description__ = "Let F ( ) be the number of strings such that: For example, F (4) = 0, " \
                          "F (5) = 8, F (6) = 42 and F (11) = 3844. Let D( ) be the number of " \
                          "integers such that 5 ≤ ≤ and F ( ) is divisible by 87654321. For " \
                          "example, D(10 ) = 0 and D(5·10 ) = 51. Find D(10 )."

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

