
__problem_title__ = "Heighway Dragon"
__problem_url___ = "https://projecteuler.net/problem=220"
__problem_description__ = "Let be the two-letter string "Fa". For n≥1, derive from by the " \
                          "string-rewriting rules: "a" → "aRbFR" "b" → "LFaLb" Thus, = "Fa", = " \
                          ""FaRbFR", = "FaRbFRRLFaLbFR", and so on. These strings can be " \
                          "interpreted as instructions to a computer graphics program, with "F" " \
                          "meaning "draw forward one unit", "L" meaning "turn left 90 degrees", " \
                          ""R" meaning "turn right 90 degrees", and "a" and "b" being ignored. " \
                          "The initial position of the computer cursor is (0,0), pointing up " \
                          "towards (0,1). Then is an exotic drawing known as the of order . For " \
                          "example, is shown below; counting each "F" as one step, the " \
                          "highlighted spot at (18,16) is the position reached after 500 steps. " \
                          "What is the position of the cursor after 10 steps in ? Give your " \
                          "answer in the form , with no spaces."

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

