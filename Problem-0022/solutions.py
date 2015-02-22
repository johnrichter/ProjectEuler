
__problem_title__ = "Names scores"
__problem_url___ = "https://projecteuler.net/problem=22"
__problem_description__ = "Using (right click and 'Save Link/Target As...'), a 46K text file " \
                          "containing over five-thousand first names, begin by sorting it into " \
                          "alphabetical order. Then working out the alphabetical value for each " \
                          "name, multiply this value by its alphabetical position in the list to " \
                          "obtain a name score. For example, when the list is sorted into " \
                          "alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, " \
                          "is the 938th name in the list. So, COLIN would obtain a score of 938 " \
                          "× 53 = 49714. What is the total of all the name scores in the file?"

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

