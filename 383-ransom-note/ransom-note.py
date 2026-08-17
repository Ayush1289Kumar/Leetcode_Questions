class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map_ransom = {}
        map_magazine = {}

        for c in ransomNote:
            map_ransom[c] = map_ransom.get(c,0)+1
        
        for c in magazine:
            map_magazine[c] = map_magazine.get(c,0)+1

        for c in map_ransom:
            if c not in map_magazine or map_magazine[c] < map_ransom[c]:
                return False
        
        return True