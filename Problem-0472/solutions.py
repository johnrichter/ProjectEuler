
__problem_title__ = "Comfortable Distance II"
__problem_url___ = "https://projecteuler.net/problem=472"
__problem_description__ = "There are seats in a row. people come one after another to fill the " \
                          "seats according to the following rules: Note that due to rule 1, some " \
                          "seats will surely be left unoccupied, and the maximum number of " \
                          "people that can be seated is less than (for > 1). Here are the " \
                          "possible seating arrangements for = 15: We see that if the first " \
                          "person chooses correctly, the 15 seats can seat up to 7 people. We " \
                          "can also see that the first person has 9 choices to maximize the " \
                          "number of people that may be seated. Let f(N) be the number of " \
                          "choices the first person has to maximize the number of occupants for " \
                          "seats in a row. Thus, f(1) = 1, f(15) = 9, f(20) = 6, and f(500) = " \
                          "16. Also, ∑f(N) = 83 for 1 ≤ ≤ 20 and ∑f(N) = 13343 for 1 ≤ ≤ 500. " \
                          "Find ∑f(N) for 1 ≤ ≤ 10 . Give the last 8 digits of your answer."

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

