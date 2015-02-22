
__problem_title__ = "Fibonacci primitive roots"
__problem_url___ = "https://projecteuler.net/problem=437"
__problem_description__ = "When we calculate 8 modulo 11 for n=0 to 9 we get: 1, 8, 9, 6, 4, 10, " \
                          "3, 2, 5, 7. As we see all possible values from 1 to 10 occur. So 8 is " \
                          "a of 11. But there is more: If we take a closer look we see: 1+8=9 " \
                          "8+9=17≡6 mod 11 9+6=15≡4 mod 11 6+4=10 4+10=14≡3 mod 11 10+3=13≡2 mod " \
                          "11 3+2=5 2+5=7 5+7=12≡1 mod 11."

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

