class BinarySearch(object):
    def __init__(self):
        self.lastGuesses = 0
        self.lastListSize = 0

    def binary_search(self, array_list, item):
        self.lastGuesses = 0
        self.lastListSize = len(array_list)
        if self.is_sorted_list(array_list):
            low = 0
            high = len(array_list) - 1
            while low <= high:
                self.lastGuesses = self.lastGuesses + 1
                mid = round((low + high) / 2)
                guess = array_list[mid]
                if guess == item:
                    return mid
                if guess > item:
                    high = mid - 1
                else:
                    low = mid + 1
        return None

    @staticmethod
    def is_sorted_list(array_list):
        aux_list = array_list.copy()
        aux_list.sort()
        return array_list == aux_list

    def last_search_result(self):
        return self.lastGuesses, self.lastListSize
