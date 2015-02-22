
__problem_title__ = "Exploring strings for which only one character comes lexicographically after its neighbour to the left"
__problem_url___ = "https://projecteuler.net/problem=158"
__problem_description__ = "Taking three different letters from the 26 letters of the alphabet, " \
                          "character strings of length three can be formed. Examples are 'abc', " \
                          "'hat' and 'zyx'. When we study these three examples we see that for " \
                          "'abc' two characters come lexicographically after its neighbour to " \
                          "the left. For 'hat' there is exactly one character that comes " \
                          "lexicographically after its neighbour to the left. For 'zyx' there " \
                          "are zero characters that come lexicographically after its neighbour " \
                          "to the left. In all there are 10400 strings of length 3 for which " \
                          "exactly one character comes lexicographically after its neighbour to " \
                          "the left. We now consider strings of ≤ 26 different characters from " \
                          "the alphabet. For every , p( ) is the number of strings of length for " \
                          "which exactly one character comes lexicographically after its " \
                          "neighbour to the left. What is the maximum value of p( )?"

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

