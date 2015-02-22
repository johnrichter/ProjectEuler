
__problem_title__ = "Minimal network"
__problem_url___ = "https://projecteuler.net/problem=107"
__problem_description__ = "The following undirected network consists of seven vertices and " \
                          "twelve edges with a total weight of 243. The same network can be " \
                          "represented by the matrix below. However, it is possible to optimise " \
                          "the network by removing some edges and still ensure that all points " \
                          "on the network remain connected. The network which achieves the " \
                          "maximum saving is shown below. It has a weight of 93, representing a " \
                          "saving of 243 − 93 = 150 from the original network. Using (right " \
                          "click and 'Save Link/Target As...'), a 6K text file containing a " \
                          "network with forty vertices, and given in matrix form, find the " \
                          "maximum saving which can be achieved by removing redundant edges " \
                          "whilst ensuring that the network remains connected."

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

