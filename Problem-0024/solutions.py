
__problem_title__ = "Lexicographic permutations"
__problem_url___ = "https://projecteuler.net/problem=24"
__problem_description__ = "A permutation is an ordered arrangement of objects. For example, 3124 " \
                          "is one possible permutation of the digits 1, 2, 3 and 4. If all of " \
                          "the permutations are listed numerically or alphabetically, we call it " \
                          "lexicographic order. The lexicographic permutations of 0, 1 and 2 " \
                          "are: 012 021 102 120 201 210 What is the millionth lexicographic " \
                          "permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"

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

