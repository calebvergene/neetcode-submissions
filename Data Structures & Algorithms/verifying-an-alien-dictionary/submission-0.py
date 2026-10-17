class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alphabet_order = {}
        for c in range(26):
            alphabet_order[order[c]] = c
        
        for i in range(len(words)-1):
            # compare this word to the next word 
            word1, word2 = words[i], words[i+1]

            print(word1, word2)

            for i in range(max(len(word1), len(word2))):
                # same sub words
                if i >= len(word2): # word one longer than word two
                    return False 
                elif i >= len(word1):
                    break

                if alphabet_order[word1[i]] > alphabet_order[word2[i]]:
                    return False
                elif alphabet_order[word1[i]] < alphabet_order[word2[i]]:
                    break

        return True