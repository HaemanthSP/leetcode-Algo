class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occurrence = {}  # Record of previous occurrence of unique elements
        seq_s = -1  # Start index of the sequence
        max_len = 0  # Maximun sequence length
        for idx, x in enumerate(s):

            if x not in occurrence:
                # On first occurrence
                occurrence[x] = idx
                
            else:
                # On occurrence with in the current sequence scope
                if occurrence[x] >= seq_s:
                    seq_s = occurrence[x]

                # Update the current occurrence
                occurrence[x] = idx
                
            # Update the max sequence length
            seq_len = idx - seq_s
            max_len = max(max_len, seq_len)
                
        return max_len        