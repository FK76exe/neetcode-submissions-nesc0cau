import string

CHAR_LIST = [chr(i) for i in range(256)]

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "None"
        encoded_str = ""
        for j, word in enumerate(strs):
            encoded_word = ""
            for i, char in enumerate(word):
                char_value = CHAR_LIST.index(char)
                encoded_word += str(char_value)
                if i != len(word) - 1:
                    encoded_word += "."
            encoded_str += encoded_word
            if j != len(strs) -1:
                encoded_str += ","
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        strs = []
        encoded_strs = s.split(",")
        for word in encoded_strs:
            decoded_word = ""
            split_word = word.split(".")
            if len(word) > 0:
                for char in split_word:
                    decoded_word += CHAR_LIST[int(char)]
            strs.append(decoded_word)
        return strs