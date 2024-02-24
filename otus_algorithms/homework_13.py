class HashTable:
    """Класс реализации хэш-таблицы."""
    DEFAULT_LOAD_FACTOR = 0.75

    def __init__(self):
        self.size = 100
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def __hash_function(self, key):
        return hash(key) % self.size

    def __get_index(self, key):
        hash_value = self.__hash_function(key)
        current_index = hash_value

        while self.keys[current_index] is not None:
            if self.keys[current_index] == key:
                return current_index
            current_index = (current_index + 1) % self.size

        return current_index

    def __get(self, key):
        index = self.__get_index(key)
        return self.values[index] if self.keys[index] == key else None

    def __put(self, key, value):
        index = self.__get_index(key)
        self.keys[index] = key
        self.values[index] = value

    def __del(self, key):
        index = self.__get_index(key)
        if self.keys[index] == key:
            self.keys[index] = None
            self.values[index] = None

    def __resize(self):
        self.size *= 2
        old_keys = self.keys
        old_values = self.values

        self.keys = [None] * self.size
        self.values = [None] * self.size

        for key, value in zip(old_keys, old_values):
            if key is not None:
                self.__put(key, value)

    def __rehash(self):
        if sum(
                True for key in self.keys if key is not None
        ) / self.size > HashTable.DEFAULT_LOAD_FACTOR:
            self.__resize()

    def get(self, key):
        return self.__get(key)

    def put(self, key, value):
        self.__put(key, value)

    def delete(self, key):
        self.__del(key)
