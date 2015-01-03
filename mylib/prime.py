import math


class Prime:
    def __init__(self):
        self.prime_list = []
        self.v = 2

    def get_prime(self):
        while True:
            for i in self.prime_list:
                if self.v % i == 0:
                    break
                elif i * i > self.v:
                    break
            else:
                self.prime_list.append(self.v)
                yield self.v
            self.v += 1

    def get_prime_list_size(self):
        return len(self.prime_list)

