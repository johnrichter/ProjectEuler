
__problem_title__ = "Gathering the beans"
__problem_url___ = "https://projecteuler.net/problem=335"
__problem_description__ = "Whenever Peter feels bored, he places some bowls, containing one bean " \
                          "each, in a circle. After this, he takes all the beans out of a " \
                          "certain bowl and drops them one by one in the bowls going clockwise. " \
                          "He repeats this, starting from the bowl he dropped the last bean in, " \
                          "until the initial situation appears again. For example with 5 bowls " \
                          "he acts as follows: So with 5 bowls it takes Peter 15 moves to return " \
                          "to the initial situation. Let ( ) represent the number of moves " \
                          "required to return to the initial situation, starting with bowls. " \
                          "Thus, (5) = 15. It can also be verified that (100) = 10920. Find (2 " \
                          "+1). Give your answer modulo 7 ."

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

