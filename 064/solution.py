#! encoding: utf8
from profile_decorate import profile
from itertools import count

"""
"""


def is_odd_period(s):
    m = [0]
    d = [1]
    a = list()
    for x in count(1):
        power = x*x
        if power == s:
            return False
        elif x*x > s:
            a.append(x-1)
            break

    for n in count(1):
        m.append(d[n-1]*a[n-1]-m[n-1])
        d.append((s-m[n]*m[n])/d[n-1])
        a.append(int((a[0]+m[n])/d[n]))
        if a[n] == a[0]*2:
            break

    if (len(a)-1)%2 != 0:
        return True
    else:
        return False


@profile
def main():
    result = 0
    for i in range(1, 10001):
        if is_odd_period(i):
            result += 1
    print("result is {}".format(result))


if __name__ == '__main__':
    main()
