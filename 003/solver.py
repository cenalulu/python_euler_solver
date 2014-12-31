class Prime:
    def __init__(self):
        self.prime_list = [1, 2]
        self.v = 3

    def get_prime(self):
        while True:
            if self.v % 2 == 0:
                self.v += 1
                continue
            for i in range(3, self.v):
                if self.v % i == 0 and i not in self.prime_list:
                    break
            else:
                self.prime_list.append(self.v)
                yield self.v
            self.v += 1


prime_list = Prime()
n_to_solve = 600851475143
while n_to_solve != 1:
    for i in prime_list.get_prime():
        if n_to_solve % i == 0:
            n_to_solve /= i
            print i, n_to_solve
            break
