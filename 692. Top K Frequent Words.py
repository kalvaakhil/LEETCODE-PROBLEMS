class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i[0] for i in collections.Counter(sorted(words)).most_common(k)]
