
__problem_title__ = "Factorisation triples"
__problem_url___ = "https://projecteuler.net/problem=418"
__problem_description__ = "Let be a positive integer. An integer triple ( , , ) is called a of " \
                          "if: Define ( ) to be + + for the factorisation triple ( , , ) of " \
                          "which minimises / . One can show that this triple is unique. For " \
                          "example, (165) = 19, (100100) = 142 and (20!) = 4034872. Find (43!)."

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

