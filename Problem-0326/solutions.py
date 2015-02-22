
__problem_title__ = "Modulo Summations"
__problem_url___ = "https://projecteuler.net/problem=326"
__problem_description__ = "Let be a sequence recursively defined by: . So the first 10 elements " \
                          "of are: 1,1,0,3,0,3,5,4,1,9. Let ( ) represent the number of pairs ( " \
                          ") such that: It can be seen that (10,10)=4 with the pairs (3,3), " \
                          "(5,5), (7,9) and (9,10). You are also given that (10 ,10 )=97158. " \
                          "Find (10 ,10 )."

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

