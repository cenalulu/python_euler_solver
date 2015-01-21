#! encoding: utf8
from profile_decorate import profile

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""


@profile
def main():
    max_p_solution = 0
    max_solution_p = 0
    for p in range(5, 1001):
        current_p_solution = 0
        # assuming a is the shortest sides
        for a in range(1, p / 3):
            for b in range(a + 1, (p - a) / 2 + 1):
                c = p - a - b
                if c ** 2 == b ** 2 + a ** 2 and a < b < c:
                    current_p_solution += 1
                    # print 'for p: {} we found a combination: {},{},{}'.format(p,a,b,c)
        if current_p_solution > max_p_solution:
            max_solution_p = p
            max_p_solution = max(max_p_solution, current_p_solution)
    print '{} is the number of max solutions'.format(max_solution_p)


if __name__ == '__main__':
    main()
