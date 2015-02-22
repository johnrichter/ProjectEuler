
__problem_title__ = "Cardano Triplets"
__problem_url___ = "https://projecteuler.net/problem=251"
__problem_description__ = "A triplet of positive integers ( , , ) is called a Cardano Triplet if " \
                          "it satisfies the condition: For example, (2,1,5) is a Cardano " \
                          "Triplet. There exist 149 Cardano Triplets for which + + ≤ 1000. Find " \
                          "how many Cardano Triplets exist such that + + ≤ 110,000,000."

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

