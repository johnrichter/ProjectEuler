
__problem_title__ = "Squarefree factors"
__problem_url___ = "https://projecteuler.net/problem=362"
__problem_description__ = "Consider the number 54. 54 can be factored in 7 distinct ways into " \
                          "one or more factors larger than 1: 54, 2×27, 3×18, 6×9, 3×3×6, 2×3×9 " \
                          "and 2×3×3×3. If we require that the factors are all squarefree only " \
                          "two ways remain: 3×3×6 and 2×3×3×3. Let's call Fsf( ) the number of " \
                          "ways can be factored into one or more squarefree factors larger than " \
                          "1, so Fsf(54)=2. Let S( ) be ∑Fsf( ) for =2 to . S(100)=193. Find " \
                          "S(10 000 000 000)."

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

