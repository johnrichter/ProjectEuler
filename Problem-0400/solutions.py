
__problem_title__ = "Fibonacci tree game"
__problem_url___ = "https://projecteuler.net/problem=400"
__problem_description__ = "A is a binary tree recursively defined as: On such a tree two players " \
                          "play a take-away game. On each turn a player selects a node and " \
                          "removes that node along with the subtree rooted at that node. The " \
                          "player who is forced to take the root node of the entire tree loses. " \
                          "Here are the winning moves of the first player on the first turn for " \
                          "T( ) from =1 to =6. For example, (5) = 1 and (10) = 17. Find (10000). " \
                          "Give the last 18 digits of your answer."

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

