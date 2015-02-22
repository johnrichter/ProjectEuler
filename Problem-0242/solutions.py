
__problem_title__ = "Odd Triplets"
__problem_url___ = "https://projecteuler.net/problem=242"
__problem_description__ = "Given the set {1,2,..., }, we define ( , ) as the number of its " \
                          "-element subsets with an odd sum of elements. For example, (5,3) = 4, " \
                          "since the set {1,2,3,4,5} has four 3-element subsets having an odd " \
                          "sum of elements, i.e.: {1,2,4}, {1,3,5}, {2,3,4} and {2,4,5}. When " \
                          "all three values , and ( , ) are odd, we say that they make an [ , , " \
                          "( , )]. There are exactly five odd-triplets with ≤ 10, namely: [1,1, " \
                          "(1,1) = 1], [5,1, (5,1) = 3], [5,5, (5,5) = 1], [9,1, (9,1) = 5] and " \
                          "[9,9, (9,9) = 1]. How many odd-triplets are there with ≤ 10 ?"

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

