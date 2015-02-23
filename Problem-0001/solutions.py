
__problem_title__ = "Multiples of 3 and 5"
__problem_url___ = "https://projecteuler.net/problem=1"
__problem_description__ = "If we list all the natural numbers below 10 that are multiples of 3 " \
                          "or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find " \
                          "the sum of all the multiples of 3 or 5 below 1000."

import timeit


class Solution():

    @staticmethod
    def solution1(below_num, m1, m2):
        multiples = [num for num in range(1, below_num) if num % m1 == 0 or num % m2 == 0]
        return sum(multiples)

    @staticmethod
    def solution2(below_num, m1, m2):
        multiples = set()
        for num in range(1, below_num):
            m1_multiple = num * m1
            m2_multiple = num * m2

            if m1_multiple >= below_num and m2_multiple >= below_num:
                break
            if m1_multiple < below_num:
                multiples.add(m1_multiple)
            if m2_multiple < below_num:
                multiples.add(m2_multiple)

        return sum(multiples)

    @staticmethod
    def solution3(below_num, m1, m2):
        multiples_sum = 0
        max_boundary = below_num - 1
        m3 = m1 * m2

        for n in range(1, max_boundary // m1 + 1):
            multiples_sum += n * m1
        for n in range(1, max_boundary // m2 + 1):
            multiples_sum += n * m2
        for n in range(1, max_boundary // m3 + 1):
            multiples_sum -= n * m3

        return multiples_sum

    @staticmethod
    def solution4(below_num, m1, m2):
        multiples_sum = 0
        max_boundary = below_num - 1
        m3 = m1 * m2

        # n(n+1)/2
        n1 = max_boundary // m1
        n2 = max_boundary // m2
        n3 = max_boundary // m3

        multiples_sum += m1 * (n1 * (n1 + 1) / 2)
        multiples_sum += m2 * (n2 * (n2 + 1) / 2)
        multiples_sum -= m3 * (n3 * (n3 + 1) / 2)

        return multiples_sum

    @staticmethod
    def time_solutions(runs):
        setup = 'from __main__ import Solution'
        print('Solution 1:',
              timeit.timeit('Solution.solution1(1000, 3, 5)', setup=setup, number=runs))
        print('Solution 2:',
              timeit.timeit('Solution.solution2(1000, 3, 5)', setup=setup, number=runs))
        print('Solution 3:',
              timeit.timeit('Solution.solution3(1000, 3, 5)', setup=setup, number=runs))
        print('Solution 4:',
              timeit.timeit('Solution.solution4(1000, 3, 5)', setup=setup, number=runs))


if __name__ == '__main__':
    s = Solution()
    print(s.solution1(1000, 3, 5))
    print(s.solution2(1000, 3, 5))
    print(s.solution3(1000, 3, 5))
    print(s.solution4(1000, 3, 5))
    s.time_solutions(50000)
