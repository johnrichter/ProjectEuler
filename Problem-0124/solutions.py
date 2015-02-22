
__problem_title__ = "Ordered radicals"
__problem_url___ = "https://projecteuler.net/problem=124"
__problem_description__ = "The radical of , rad( ), is the product of the distinct prime factors " \
                          "of . For example, 504 = 2 × 3 × 7, so rad(504) = 2 × 3 × 7 = 42. If " \
                          "we calculate rad( ) for ≤ ≤ 10, then sort them on rad( ), and sorting " \
                          "on if the radical values are equal, we get: Let E( ) be the th " \
                          "element in the sorted column; for example, E(4) = 8 and E(6) = 9. If " \
                          "rad( ) is sorted for 1 ≤ ≤ 100000, find E(10000)."

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

