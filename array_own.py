class MyArray:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")


def main():
    array = MyArray(3)
    array.set(0, "Hola")
    array.set(2, "Adios")
    print(array.get(0))
    print(array.get(1))
    print(array.get(2))


main()
