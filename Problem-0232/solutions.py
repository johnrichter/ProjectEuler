
__problem_title__ = "The Race"
__problem_url___ = "https://projecteuler.net/problem=232"
__problem_description__ = "Two players share an unbiased coin and take it in turns to play "The " \
                          "Race". On Player 1's turn, he tosses the coin once: if it comes up " \
                          "Heads, he scores one point; if it comes up Tails, he scores nothing. " \
                          "On Player 2's turn, she chooses a positive integer and tosses the " \
                          "coin times: if it comes up all Heads, she scores 2 points; otherwise, " \
                          "she scores nothing. Player 1 goes first. The winner is the first to " \
                          "100 or more points. On each turn Player 2 selects the number, , of " \
                          "coin tosses that maximises the probability of her winning. What is " \
                          "the probability that Player 2 wins? Give your answer rounded to eight " \
                          "decimal places in the form 0. ."

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

