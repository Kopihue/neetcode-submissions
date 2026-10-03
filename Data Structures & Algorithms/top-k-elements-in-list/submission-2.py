class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
    
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
    
        values = list(counter.values())
        reps = set()
    
        for _ in range(k):
            if not values:
                break
    
            reps.add(values.pop(values.index(max(values))))
    
        final_counter = []
        for n in counter.keys():
            if counter[n] in reps:
                final_counter.append(n)
        
        return final_counter