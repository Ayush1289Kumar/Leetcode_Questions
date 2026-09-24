import heapq


class Pair:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq

        return self.word > other.word


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:

        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        heap = []

        for word, count in freq.items():

            if len(heap) < k:
                heapq.heappush(heap, Pair(count, word))

            elif count > heap[0].freq or (
                count == heap[0].freq and word < heap[0].word
            ):
                heapq.heapreplace(heap, Pair(count, word))

        ans = []

        while heap:
            ans.append(heapq.heappop(heap).word)

        return ans[::-1]