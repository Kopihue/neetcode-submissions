class Solution:

    def encode(self, strs: List[str]) -> str:
        final_s = ""
        for word in strs:
            final_s += str(len(word)) + "$" + word
    
        return final_s

    def decode(self, s: str) -> List[str]:
        iters = iter(s)
        final_iters = []
        number = ""
    
        for c in iters:
            if c == "$":
                word = ""
                for _ in range(int(number)):
                    word += next(iters)
    
                final_iters.append(word)
                number = ""
                continue
    
            number += c

        return final_iters