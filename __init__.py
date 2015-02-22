__author__ = 'John Richter'
__problem_url_base__ = 'https://projecteuler.net/problem={number}'
__solution_template__ = """
__problem_title__ = "{title}"
__problem_url___ = "{link}"
__problem_description__ = "{description}"

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

"""

import os, requests
from lxml import html


def create_problem(number):
    """
    Create a new python package and skeleton solution file for problem :param number:
    :param number: The Project Euler problem number
    :return: None
    :raises: OSError if problem has already been created
             urllib.error.URLError, urllib.error.HTTPError if problem cannot be retrieved from
             the Project Euler website.
    """
    if problem_num <= 0:
        raise ValueError('Problem number {0} <= 0'.format(number))

    new_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                           'Problem-{0:04d}'.format(number))
    os.makedirs(new_dir)

    init_file = os.path.join(new_dir, '__init__.py')
    solutions_file = os.path.join(new_dir, 'solutions.py')

    with open(init_file, 'w') as init:
        init.write('__author__ = "John Richter"')

    with open(solutions_file, 'w') as solutions:
        # Download the problem from the Project Euler website
        pe_response = requests.get(__problem_url_base__.format(number=number))
        pe_response.raise_for_status()

        # Process the response as XML and extract problem details
        root = html.fromstring(pe_response.text)
        problem_title = ' '.join(root.xpath('./body/div/div[@id="content"]/h2/text()'))
        problem_info = ' '.join(root.xpath('./body/div/div/div[@role="problem"]/p/text()'))

        # I have no words for how DIRTY this is, but it works. TODO: clean it up
        problem_desc_lines = []
        current_line_len = 26 + 2    # 26 space indent, 2 quotes
        current_line = ""
        for word in problem_info.split():
            if current_line_len + len(word) + 2 > 98:  # quote and a space
                problem_desc_lines.append(current_line + ' " \\')
                current_line = " "*26 + '"' + word
                current_line_len = 26 + 2 + len(word)    # 26 space indent, 2 quotes
            elif current_line_len == 26 + 2:
                current_line += word
                current_line_len += len(word)
            else:
                current_line += " " + word
                current_line_len += 1 + len(word)

        problem_desc_lines.append(current_line)

        problem_desc = '\n'.join(problem_desc_lines)

        # Format the file templates
        problem_url = __problem_url_base__.format(number=number)
        template = __solution_template__.format(
            title=problem_title,
            link=problem_url,
            description=problem_desc
        )

        # Create the solutions.py skeleton file.
        solutions.write(template)


if __name__ == '__main__':
    from requests.exceptions import HTTPError

    for problem_num in range(1, 505):  # 505
        try:
            create_problem(problem_num)
        except ValueError as e:
            print(e)
        except OSError as e:
            print("Problem exists. Skipping creation of problem {0}".format(problem_num))
        except HTTPError as e:
            print("Cannot retrieve problem {0}".format(problem_num), e)
        except Exception as e:
            print(e)
