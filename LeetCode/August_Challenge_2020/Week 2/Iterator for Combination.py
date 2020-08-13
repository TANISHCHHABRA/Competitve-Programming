class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combos = list(itertools.combinations(characters, combinationLength))
        self.i = 0
        

    def next(self) -> str:
        combo = "".join(self.combos[self.i])
        self.i += 1
        return combo
        

    def hasNext(self) -> bool:
        return self.i < len(self.combos)
