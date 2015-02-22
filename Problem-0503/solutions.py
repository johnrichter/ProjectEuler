
__problem_title__ = "Compromise or persist"
__problem_url___ = "https://projecteuler.net/problem=503"
__problem_description__ = "Alice is playing a game with cards numbered 1 to . A game consists of " \
                          "iterations of the following steps. (1) Alice picks one of the cards " \
                          "at random. (2) Alice cannot see the number on it. Instead, Bob, one " \
                          "of her friends, sees the number and tells Alice how many " \
                          "previously-seen numbers are bigger than the number which he is " \
                          "seeing. (3) Alice can end or continue the game. If she decides to " \
                          "end, the number becomes her score. If she decides to continue, the " \
                          "card is removed from the game and she returns to (1). If there is no " \
                          "card left, she is forced to end the game. Let F( ) be the Alice's " \
                          "expected score if she takes the optimized strategy to her score. For " \
                          "example, F(3) = 5/3. At the first iteration, she should continue the " \
                          "game. At the second iteration, she should end the game if Bob says " \
                          "that one previously-seen number is bigger than the number which he is " \
                          "seeing, otherwise she should continue the game. We can also verify " \
                          "that F(4) = 15/8 and F(10) ≈ 2.5579365079. Find F(10 ). Give your " \
                          "answer rounded to 10 decimal places behind the decimal point."

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

