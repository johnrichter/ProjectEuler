
__problem_title__ = "Risky moon"
__problem_url___ = "https://projecteuler.net/problem=353"
__problem_description__ = "A moon could be described by the sphere C( ) with centre (0,0,0) and " \
                          "radius . There are stations on the moon at the points on the surface " \
                          "of C( ) with integer coordinates. The station at (0,0, ) is called " \
                          "North Pole station, the station at (0,0,- ) is called South Pole " \
                          "station. All stations are connected with each other via the shortest " \
                          "road on the great arc through the stations. A journey between two " \
                          "stations is risky. If is the length of the road between two stations, " \
                          "( /(π )) is a measure for the risk of the journey (let us call it the " \
                          "risk of the road). If the journey includes more than two stations, " \
                          "the risk of the journey is the sum of risks of the used roads. A " \
                          "direct journey from the North Pole station to the South Pole station " \
                          "has the length π and risk 1. The journey from the North Pole station " \
                          "to the South Pole station via (0, ,0) has the same length, but a " \
                          "smaller risk: (½π /(π )) +(½π /(π )) =0.5. The minimal risk of a " \
                          "journey from the North Pole station to the South Pole station on C( ) " \
                          "is M( ). You are given that M(7)=0.1784943998 rounded to 10 digits " \
                          "behind the decimal point. Find ∑M(2 -1) for 1≤n≤15. Give your answer " \
                          "rounded to 10 digits behind the decimal point in the form " \
                          "a.bcdefghijk."

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

