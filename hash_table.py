class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                del bucket[i]
                return

        raise KeyError(f"Key '{key}' not found")


def main():
    hash_table = HashTable(size=10)
    hash_table.insert("name", "John")
    hash_table.insert("age", 25)

    print(hash_table.get("name"))
    print(hash_table.get("age"))

    hash_table.remove("age")
    print(hash_table.get("age"))


main()
