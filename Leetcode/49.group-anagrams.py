#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def create_hash(word: str) -> dict:
            alphabets = {}
            for alphabet in word:
                if alphabet in alphabets:
                    alphabets[alphabet] += 1
                else:
                    alphabets[alphabet] = 1
            return alphabets

        hash_list = [create_hash(word) for word in strs]
        output_list = []
        visited = [0 for word in strs]


        for i, hashmap in enumerate(hash_list):
            if visited[i]:
                continue
            matches = [strs[i]]
            visited[i] = 1
            for j, hashmap2 in enumerate(hash_list):
                if not visited[j] and hashmap == hashmap2:
                    matches.append(strs[j])
                    visited[j] = 1

            output_list.append(matches)

        return output_list


# @lc code=end

