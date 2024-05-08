class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort the score array in descending order along with athlete indices
        sorted_score = sorted(enumerate(score), key=lambda x: x[1], reverse=True)
        
        # Initialize an array to store ranks
        ranks = [''] * len(score)
        
        # Assign ranks to athletes based on their placement
        for i, (index, _) in enumerate(sorted_score):
            if i == 0:
                ranks[index] = "Gold Medal"
            elif i == 1:
                ranks[index] = "Silver Medal"
            elif i == 2:
                ranks[index] = "Bronze Medal"
            else:
                ranks[index] = str(i + 1)
        
        return ranks
