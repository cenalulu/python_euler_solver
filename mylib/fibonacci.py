class Fibonacci:
    def __init__(self):
        self.v1_now = 1
        self.v2_now = 1
        self.__term_num = 3

    def get_next(self):
        while True:
            yield self.v1_now + self.v2_now
            (self.v1_now, self.v2_now) = (self.v2_now, self.v1_now + self.v2_now)
            self.__term_num += 1

    def get_term_num(self):
        return self.__term_num