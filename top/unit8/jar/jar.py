class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        if (n + self.size) <= self.capacity:
            self.size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if (self.size - n) >= 0:
            self.size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    print(jar)

if __name__ == "__main__":
    main()

