from prime import Prime

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

prime_list = Prime()
prime_sum = 0

for i in prime_list.get_prime():
    if i < 2000000:
        prime_sum += i
    else:
        print prime_sum
        break


