class RandomizedSet:

    def __init__(self):
        self.ls = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.ls)
        self.ls.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        last_ele = self.ls[-1]
        val_ind = self.map[val]
        self.ls[val_ind] = last_ele
        self.map[last_ele] = val_ind
        self.ls.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.ls)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()