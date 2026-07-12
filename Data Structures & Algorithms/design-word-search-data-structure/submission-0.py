class WordDictionary:
    # trie + dfs

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        level = self.root
        for char in word:
            if char not in level:
                level[char] = {}
            level = level[char]
        level["word"] = True


    def search(self, word: str) -> bool:
        # use dfs
        def dfs(level, word):
            for char in word:
                if char == ".":
                    for key in level:
                        if key != "word":
                            return dfs(level[key], word[1:])
                else:
                    if char not in level:
                        return False
                    level = level[char]
            return level.get("word", False)
        return dfs(self.root, word)
        