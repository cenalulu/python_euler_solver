import math


class Prime:
    def __init__(self):
        self.prime_list = [2]
        self.v = 3

    def get_prime(self):
        yield 2
        while True:
            for i in self.prime_list:
                if self.v % i == 0:
                    break
                # before adding this tuning
                #to find the biggest prime less than 300000
                # 300007
                #cost: real    0m33.046s
                elif i * i > self.v + 1:
                    yield self.v
                    self.prime_list.append(self.v)
                    break
            else:
                self.prime_list.append(self.v)
                yield self.v
            self.v += 2

    def get_prime_list_size(self):
        return len(self.prime_list)


if __name__ == '__main__':
    prime_under = 2000000
    prime_list = Prime()
    for i in prime_list.get_prime():
        if i > prime_under:
            print i
            break

