
__problem_title__ = "Chef Showdown"
__problem_url___ = "https://projecteuler.net/problem=481"
__problem_description__ = "A group of chefs (numbered #1, #2, etc) participate in a turn-based " \
                          "strategic cooking competition. On each chef's turn, he/she cooks up a " \
                          "dish to the best of his/her ability and gives it to a separate panel " \
                          "of judges for taste-testing. Let S( ) represent chef # 's skill level " \
                          "(which is publicly known). More specifically, S( ) is the probability " \
                          "that chef # 's dish will be assessed favorably by the judges (on " \
                          "any/all turns). If the dish receives a favorable rating, then the " \
                          "chef must choose one other chef to be eliminated from the " \
                          "competition. The last chef remaining in the competition is the " \
                          "winner. The game always begins with chef #1, with the turn order " \
                          "iterating sequentially over the rest of the chefs still in play. Then " \
                          "the cycle repeats from the lowest-numbered chef. All chefs aim to " \
                          "optimize their chances of winning within the rules as stated, " \
                          "assuming that the other chefs behave in the same manner. In the event " \
                          "that a chef has more than one equally-optimal elimination choice, " \
                          "assume that the chosen chef is always the one with the next-closest " \
                          "turn. Define W ( ) as the probability that chef # wins in a " \
                          "competition with chefs. If we have S(1) = 0.25, S(2) = 0.5, and S(3) " \
                          "= 1, then W (1) = 0.29375. Going forward, we assign S( ) = F /F over " \
                          "all 1 â¤ â¤ , where F is a Fibonacci number: F = F + F with base " \
                          "cases F = F = 1. Then, for example, when considering a competition " \
                          "with = 7 chefs, we have W (1) = 0.08965042, W (2) = 0.20775702, W (3) " \
                          "= 0.15291406, W (4) = 0.14554098, W (5) = 0.15905291, W (6) = " \
                          "0.10261412, and W (7) = 0.14247050, rounded to 8 decimal places each. " \
                          "Let E( ) represent the expected number of dishes cooked in a " \
                          "competition with chefs. For instance, E(7) = 42.28176050. Find E(14) " \
                          "rounded to 8 decimal places."

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

