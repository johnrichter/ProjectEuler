
__problem_title__ = "Badugi"
__problem_url___ = "https://projecteuler.net/problem=369"
__problem_description__ = "In a standard 52 card deck of playing cards, a set of 4 cards is a if " \
                          "it contains 4 cards with no pairs and no two cards of the same suit. " \
                          "Let f( ) be the number of ways to choose cards with a 4 card subset " \
                          "that is a Badugi. For example, there are 2598960 ways to choose five " \
                          "cards from a standard 52 card deck, of which 514800 contain a 4 card " \
                          "subset that is a Badugi, so f(5) = 514800. Find ∑f( ) for 4 ≤ ≤ 13."

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

