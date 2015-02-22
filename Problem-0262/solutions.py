
__problem_title__ = "Mountain Range"
__problem_url___ = "https://projecteuler.net/problem=262"
__problem_description__ = "The following equation represents the topography of a mountainous " \
                          "region, giving the at any point ( , ): A mosquito intends to fly from " \
                          "A(200,200) to B(1400,1400), without leaving the area given by 0 ≤ , ≤ " \
                          "1600. Because of the intervening mountains, it first rises straight " \
                          "up to a point A', having elevation . Then, while remaining at the " \
                          "same elevation , it flies around any obstacles until it arrives at a " \
                          "point B' directly above B. First, determine which is the minimum " \
                          "constant elevation allowing such a trip from A to B, while remaining " \
                          "in the specified area. Then, find the length of the shortest path " \
                          "between A' and B', while flying at that constant elevation . Give " \
                          "that length as your answer, rounded to three decimal places."

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

