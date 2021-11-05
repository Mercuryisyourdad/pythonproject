class LCG(object):
    def __init__(self, seed: int, multiplier: int, increment: int, modulus: int):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        self.x = seed

    def getSeed(self):
        return self.seed

    def setSeed(self, seed: int):
        self.seed = seed

    def initialize(self):
        self.x = self.seed

    def next(self):
        ans = self.x / self.modulus
        self.x = (self.multiplier * self.x + self.increment) % self.modulus
        return ans

    def getSequence(self, seq_len: int):
        seq = []
        for _ in range(seq_len):
            seq.append(self.next())
        return seq
