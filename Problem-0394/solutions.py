
__problem_title__ = "Eating pie"
__problem_url___ = "https://projecteuler.net/problem=394"
__problem_description__ = "Jeff eats a pie in an unusual way. The pie is circular. He starts " \
                          "with slicing an initial cut in the pie along a radius. While there is " \
                          "at least a given fraction of pie left, he performs the following " \
                          "procedure: - He makes two slices from the pie centre to any point of " \
                          "what is remaining of the pie border, any point on the remaining pie " \
                          "border equally likely. This will divide the remaining pie into three " \
                          "pieces. - Going counterclockwise from the initial cut, he takes the " \
                          "first two pie pieces and eats them. When less than a fraction of pie " \
                          "remains, he does not repeat this procedure. Instead, he eats all of " \
                          "the remaining pie. For ≥ 1, let E( ) be the expected number of times " \
                          "Jeff repeats the procedure above with = / . It can be verified that " \
                          "E(1) = 1, E(2) ≈ 1.2676536759, and E(7.5) ≈ 2.1215732071. Find E(40) " \
                          "rounded to 10 decimal places behind the decimal point."

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

