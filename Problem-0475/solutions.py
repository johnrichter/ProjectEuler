
__problem_title__ = "Music festival"
__problem_url___ = "https://projecteuler.net/problem=475"
__problem_description__ = "12 musicians participate at a music festival. On the first day, they " \
                          "form 3 quartets and practice all day. It is a disaster. At the end of " \
                          "the day, all musicians decide they will never again agree to play " \
                          "with any member of their quartet. On the second day, they form 4 " \
                          "trios, each musician avoiding his previous quartet partners. Let (12 " \
                          ") be the number of ways to organize the trios amongst the 12 " \
                          "musicians. You are given (12) = 576 and (24) mod 1 000 000 007 = " \
                          "509089824. Find (600) mod 1 000 000 007."

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

