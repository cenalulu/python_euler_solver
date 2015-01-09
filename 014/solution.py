# encoding: utf8
"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
cache_list = {1: 1}
max_chain_length = 0
max_chain_number = 0

for n in xrange(2, 1000000):
    next_value = n
    current_chain_length = 0
    while True:
        if next_value in cache_list:
            current_chain_length += cache_list[next_value]
            cache_list[n] = current_chain_length
            if current_chain_length > max_chain_length:
                max_chain_length = current_chain_length
                max_chain_number = n
            break
        else:
            current_chain_length += 1

        if next_value % 2 == 0:
            next_value /= 2
        else:
            next_value = next_value * 3 + 1

print max_chain_number, max_chain_length

