class Jar:

    def __init__(self, capacity=12):

        self.capacity=capacity
        self._size = 0
    def __str__(self):
        return self._size*"🍪"

    def deposit(self, n):
        if n+self.size>self.capacity:
            raise ValueError
        self._size+=n

    def withdraw(self, n):
        if self.size-n<0:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self,capacity):
        if capacity<0:
            raise ValueError("wrong capacity")
        self._capacity=capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        self._size=size
