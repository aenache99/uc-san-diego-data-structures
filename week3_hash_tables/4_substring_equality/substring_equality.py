class Solver:
    def __init__(self, s):
        self.s = s
        self.base = 256  # Base for rolling hash
        self.mod = 10 ** 9 + 7  # Modulus for rolling hash
        self.powers = [1] * (len(s) + 1)  # Include an extra element
        for i in range(1, len(s) + 1):
            self.powers[i] = (self.powers[i - 1] * self.base) % self.mod
        self.hash_values = [0] * (len(s) + 1)
        for i in range(len(s)):
            self.hash_values[i + 1] = (self.hash_values[i] * self.base + ord(s[i])) % self.mod

    def calculate_hash(self, start, length):
        end = start + length
        hash_value = (self.hash_values[end] - self.hash_values[start] * self.powers[length]) % self.mod
        return hash_value

    def ask(self, a, b, l):
        hash_a = self.calculate_hash(a, l)
        hash_b = self.calculate_hash(b, l)
        return hash_a == hash_b


s = input().strip()
q = int(input().strip())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, input().strip().split())
    print("Yes" if solver.ask(a, b, l) else "No")
