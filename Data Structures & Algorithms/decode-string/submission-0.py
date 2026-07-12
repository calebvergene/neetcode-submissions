class Solution:
    def decodeString(self, s: str) -> str:
        # when you hit a "]", go back into the stack until you find a "["

        # keep another stack to store each "[" index then remove with string splice

        brackets = []
        final_word = ""
        
        for c in s:
            print(final_word)
            # store the indexes of opening brackets
            if c == "[":
                brackets.append(len(final_word))
                final_word += c
            # if its a closing, then find the number and then multiply the string splice
            elif c == "]":
                closing = brackets.pop()-1 # points to number
                num = int(s[closing])
                # cut out the decoded part
                decoded = final_word[closing+2:]
                final_word = final_word[:closing]
                # now add the string 
                final_word += (decoded*num)
            # else, just add the char to final word 
            else:
                final_word += c
        return final_word
