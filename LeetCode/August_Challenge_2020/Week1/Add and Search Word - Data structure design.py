class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sizetowords = {}

    
    def comparesok(self, w1, w2):
        for i in range(len(w1)):
            if w2[i]!='.' and w1[i]!=w2[i]:
                return False
        return True
            
    def searchwordlist2(self, words, word):
        for w in words:
            if self.comparesok(w, word):
                return True
        return False
    
    def searchwordlist(self, words, word):
        #print ("Testing word ", word)
        if '.' not in word:
            return word in words
        for i in range(len(word)):
            if word[i]!='.':
                continue
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'a' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'b' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'c' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'd' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'e' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'f' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'g' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'h' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'i' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'j' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'k' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'l' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'm' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'n' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'o' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'p' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'q' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'r' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 's' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 't' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'u' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'v' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'w' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'x' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'y' + word[i+1:]):
                return True
            if self.searchwordlist(words, word[0:i] + 'x' + word[i+1:]):
                return True
            
        return False
    
    
    def addWord(self, word: str) -> None:
        if  len(word) not in self.sizetowords:
            self.sizetowords[len(word)] = {}
        self.sizetowords[len(word)][word] = True  
        # print("Dict ", self.sizetowords)
        
    def search(self, word: str) -> bool:
        if len(word) not in self.sizetowords:
            return False
        if word in self.sizetowords[len(word)]:
            return True
        return self.searchwordlist2(self.sizetowords[len(word)], word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
