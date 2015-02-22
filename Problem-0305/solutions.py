
__problem_title__ = "Reflexive Position"
__problem_url___ = "https://projecteuler.net/problem=305"
__problem_description__ = "Let's call S the (infinite) string that is made by concatenating the " \
                          "consecutive positive integers (starting from 1) written down in base " \
                          "10. Thus, S = 1234567891011121314151617181920212223242... It's easy " \
                          "to see that any number will show up an infinite number of times in S. " \
                          "Let's call f(n) the starting position of the n occurrence of n in S. " \
                          "For example, f(1)=1, f(5)=81, f(12)=271 and f(7780)=111111365. Find " \
                          "∑f(3 ) for 1≤k≤13."

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

