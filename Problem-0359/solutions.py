
__problem_title__ = "Hilbert's New Hotel"
__problem_url___ = "https://projecteuler.net/problem=359"
__problem_description__ = "An infinite number of people (numbered 1, 2, 3, etc.) are lined up to " \
                          "get a room at Hilbert's newest infinite hotel. The hotel contains an " \
                          "infinite number of floors (numbered 1, 2, 3, etc.), and each floor " \
                          "contains an infinite number of rooms (numbered 1, 2, 3, etc.). " \
                          "Initially the hotel is empty. Hilbert declares a rule on how the " \
                          "person is assigned a room: person gets the first vacant room in the " \
                          "lowest numbered floor satisfying either of the following: Person 1 " \
                          "gets room 1 in floor 1 since floor 1 is empty. Person 2 does not get " \
                          "room 2 in floor 1 since 1 + 2 = 3 is not a perfect square. Person 2 " \
                          "instead gets room 1 in floor 2 since floor 2 is empty. Person 3 gets " \
                          "room 2 in floor 1 since 1 + 3 = 4 is a perfect square. Eventually, " \
                          "every person in the line gets a room in the hotel. Define P( , ) to " \
                          "be if person occupies room in floor , and 0 if no person occupies the " \
                          "room. Here are a few examples: P(1, 1) = 1 P(1, 2) = 3 P(2, 1) = 2 " \
                          "P(10, 20) = 440 P(25, 75) = 4863 P(99, 100) = 19454 Find the sum of " \
                          "all P( , ) for all positive and such that × = 71328803586048 and give " \
                          "the last 8 digits as your answer."

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

