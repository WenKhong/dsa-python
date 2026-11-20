def longestConsecutive(self, nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    longest = 0
    for n in freq:
        if n - 1 not in freq:
            length = 0
            while n + length in freq:
                length += 1
            longest = max(longest, length)
    return longest

