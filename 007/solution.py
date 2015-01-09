class Prime:
    def __init__(self):
        self.prime_list = [2]
        self.v = 3

    def get_prime(self):
        while True:
            if self.v % 2 == 0:
                self.v += 1
                continue
            for i in self.prime_list:
                if self.v % i == 0:
                    break
            else:
                self.prime_list.append(self.v)
                yield self.v
            self.v += 1

    def get_prime_list_size(self):
        return len(self.prime_list)


prime = Prime()
for i in prime.get_prime():
    print prime.get_prime_list_size()
    if prime.get_prime_list_size() == 10001:
        print i
        break
