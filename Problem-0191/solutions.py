
__problem_title__ = "Prize Strings"
__problem_url___ = "https://projecteuler.net/problem=191"
__problem_description__ = "A particular school offers cash rewards to children with good " \
                          "attendance and punctuality. If they are absent for three consecutive " \
                          "days or late on more than one occasion then they forfeit their prize. " \
                          "During an n-day period a trinary string is formed for each child " \
                          "consisting of L's (late), O's (on time), and A's (absent). Although " \
                          "there are eighty-one trinary strings for a 4-day period that can be " \
                          "formed, exactly forty-three strings would lead to a prize: OOOO OOOA " \
                          "OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA OAOL OAAO OAAL OALO OALA OLOO " \
                          "OLOA OLAO OLAA AOOO AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL " \
                          "AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA LAOO LAOA LAAO How " \
                          "many "prize" strings exist over a 30-day period?"

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

