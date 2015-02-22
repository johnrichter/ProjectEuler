
__problem_title__ = "1000-digit Fibonacci number"
__problem_url___ = "https://projecteuler.net/problem=25"
__problem_description__ = "The Fibonacci sequence is defined by the recurrence relation: Hence " \
                          "the first 12 terms will be: The 12th term, F , is the first term to " \
                          "contain three digits. What is the first term in the Fibonacci " \
                          "sequence to contain 1000 digits?"

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

