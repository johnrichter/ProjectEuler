
__problem_title__ = "Coloured Configurations"
__problem_url___ = "https://projecteuler.net/problem=194"
__problem_description__ = "Consider graphs built with the units A: and B: , where the units are " \
                          "glued along the vertical edges as in the graph . A configuration of " \
                          "type ( , , ) is a graph thus built of units A and units B, where the " \
                          "graph's vertices are coloured using up to colours, so that no two " \
                          "adjacent vertices have the same colour. The compound graph above is " \
                          "an example of a configuration of type (2,2,6), in fact of type (2,2, " \
                          ") for all ≥ 4. Let N( , , ) be the number of configurations of type ( " \
                          ", , ). For example, N(1,0,3) = 24, N(0,2,4) = 92928 and N(2,2,3) = " \
                          "20736. Find the last 8 digits of N(25,75,1984)."

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

