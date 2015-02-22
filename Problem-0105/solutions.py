
__problem_title__ = "Special subset sums: testing"
__problem_url___ = "https://projecteuler.net/problem=105"
__problem_description__ = "Let S(A) represent the sum of elements in set A of size . We shall " \
                          "call it a special sum set if for any two non-empty disjoint subsets, " \
                          "B and C, the following properties are true: For example, {81, 88, 75, " \
                          "42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = " \
                          "75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} " \
                          "satisfies both rules for all possible subset pair combinations and " \
                          "S(A) = 1286. Using (right click and "Save Link/Target As..."), a 4K " \
                          "text file with one-hundred sets containing seven to twelve elements " \
                          "(the two examples given above are the first two sets in the file), " \
                          "identify all the special sum sets, A , A , ..., A , and find the " \
                          "value of S(A ) + S(A ) + ... + S(A ). NOTE: This problem is related " \
                          "to and ."

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

