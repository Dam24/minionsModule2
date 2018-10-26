class ArrayList(object):

    def __init__(self, length=5):
        self.list = [None] * length
        self.items = 0

    def append(self, value):
        if self.items >= len(self.list):
            aux_list = [0] * (len(self.list) + 1)
            index = 0
            while index < len(self.list):
                aux_list[index] = self.list[index]
                index = index + 1
            self.list = aux_list

        self.list[self.items] = value
        self.items = self.items + 1

    def search(self, index=None, value=None):
        if index:
            return self.list[index]
        index = 0
        while index < len(self.list):
            if self.list[index] == value:
                return self.list[index]
            index = index + 1

        raise ValueError("Data not in list")
