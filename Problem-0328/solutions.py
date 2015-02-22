
__problem_title__ = "Lowest-cost Search"
__problem_url___ = "https://projecteuler.net/problem=328"
__problem_description__ = "We are trying to find a hidden number selected from the set of " \
                          "integers {1, 2, ..., } by asking questions. Each number (question) we " \
                          "ask, has a and we get one of three possible answers: Given the value " \
                          "of , an minimizes the total cost (i.e. the sum of all the questions " \
                          "asked) . E.g. If =3, the best we can do is obviously to ask the " \
                          "number " ". The answer will immediately lead us to find the hidden " \
                          "number (at a total cost = 2). If =8, we might decide to use a "binary " \
                          "search" type of strategy: Our first question would be " " and if the " \
                          "hidden number is higher than 4 we will need one or two additional " \
                          "questions. Let our second question be " ". If the hidden number is " \
                          "still higher than 6, we will need a third question in order to " \
                          "discriminate between 7 and 8. Thus, our third question will be " " " \
                          "and the total cost for this worst-case scenario will be 4+6+7= . We " \
                          "can improve considerably the worst-case cost for =8, by asking " " as " \
                          "our first question. If we are told that the hidden number is higher " \
                          "than 5, our second question will be " ", then we'll know for certain " \
                          "what the hidden number is (for a total cost of 5+7= ). If we are told " \
                          "that the hidden number is lower than 5, our second question will be " " \
                          "" and if the hidden number is lower than 3 our third question will be " \
                          "" ", giving a total cost of 5+3+1= . Since > , the worst-case cost " \
                          "for this strategy is . That's better than what we achieved previously " \
                          "with the "binary search" strategy; it is also better than or equal to " \
                          "any other strategy. So, in fact, we have just described an optimal " \
                          "strategy for =8. Let C( ) be the worst-case cost achieved by an " \
                          "optimal strategy for , as described above. Thus C(1) = 0, C(2) = 1, " \
                          "C(3) = 2 and C(8) = 12. Similarly, C(100) = 400 and C( ) = 17575. " \
                          "Find C( )."

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

