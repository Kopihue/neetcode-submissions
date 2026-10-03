class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: dict[str, list[str]] = {}

        for word in strs:
            sw = "".join(sorted(word))
    
            if sw in anagrams:
                anagrams[sw].append(word)
            else:
                anagrams[sw] = [word]
    
        ordered_anagrams = []
        for anagram in anagrams.values():
            ordered_anagrams.append(anagram)
    
        return ordered_anagrams