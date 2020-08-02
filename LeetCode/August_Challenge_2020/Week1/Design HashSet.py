class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []

    def add(self, key: int) -> None:
        self.arr.append(hash(key))
    
    def remove(self, key: int) -> None:
        while self.contains(key):
            self.arr.remove(hash(key))
  
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if hash(key) in self.arr:
            return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
