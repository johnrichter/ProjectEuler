
__problem_title__ = "Special subset sums: meta-testing"
__problem_url___ = "https://projecteuler.net/problem=106"
__problem_description__ = "Let S(A) represent the sum of elements in set A of size . We shall " \
                          "call it a special sum set if for any two non-empty disjoint subsets, " \
                          "B and C, the following properties are true: For this problem we shall " \
                          "assume that a given set contains strictly increasing elements and it " \
                          "already satisfies the second rule. Surprisingly, out of the 25 " \
                          "possible subset pairs that can be obtained from a set for which = 4, " \
                          "only 1 of these pairs need to be tested for equality (first rule). " \
                          "Similarly, when = 7, only 70 out of the 966 subset pairs need to be " \
                          "tested. For = 12, how many of the 261625 subset pairs that can be " \
                          "obtained need to be tested for equality? NOTE: This problem is " \
                          "related to and ."

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

