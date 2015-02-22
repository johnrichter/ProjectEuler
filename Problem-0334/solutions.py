
__problem_title__ = "Spilling the beans"
__problem_url___ = "https://projecteuler.net/problem=334"
__problem_description__ = "In Plato's heaven, there exist an infinite number of bowls in a " \
                          "straight line. Each bowl either contains some or none of a finite " \
                          "number of beans. A child plays a game, which allows only one kind of " \
                          "move: removing two beans from any bowl, and putting one in each of " \
                          "the two adjacent bowls. The game ends when each bowl contains either " \
                          "one or no beans. For example, consider two adjacent bowls containing " \
                          "2 and 3 beans respectively, all other bowls being empty. The " \
                          "following eight moves will finish the game: You are given the " \
                          "following sequences: The first two terms of the last sequence are = " \
                          "289 and = 145. If we start with and beans in two adjacent bowls, " \
                          "3419100 moves would be required to finish the game. Consider now 1500 " \
                          "adjacent bowls containing , ,..., beans respectively, all other bowls " \
                          "being empty. Find how many moves it takes before the game ends."

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

