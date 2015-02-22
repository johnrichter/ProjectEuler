
__problem_title__ = "Average least common multiple"
__problem_url___ = "https://projecteuler.net/problem=448"
__problem_description__ = "The function (a,b) denotes the least common multiple of a and b. Let " \
                          "A(n) be the average of the values of lcm(n,i) for 1≤i≤n. E.g: " \
                          "A(2)=(2+2)/2=2 and A(10)=(10+10+30+20+10+30+70+40+90+10)/10=32. Find " \
                          "S(99999999019) mod 999999017."

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

