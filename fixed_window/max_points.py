'''
Given N cards arranged in a row, each card has an associated score denoted by the cardScore array. 
Choose exactly k cards. In each step, a card can be chosen either from the beginning or the end of the row. 
The score is the sum of the scores of the chosen cards.

Return the maximum score that can be obtained.

Example 1

Input : cardScore = [1, 2, 3, 4, 5, 6] , k = 3

Output : 15

Explanation : Choosing the rightmost cards will maximize your total score. 
So optimal cards chosen are the rightmost three cards 4 , 5 , 6.

The score is 4 + 5 + 6 => 15.
'''

class Solution:
    def maxScore(self, cardScore, k):
        #your code goes here
        # print("cardScore: ", cardScore)

        lsum = 0
        rsum = 0
        maxsum = 0

        for i in range(k):
            lsum = lsum + cardScore[i]

        maxsum = lsum

        rindex = len(cardScore) - 1
        for i in range(k-1,-1,-1):
            # print("i: ", i)
            # print("cardScore[i]: ", cardScore[i])
            lsum = lsum - cardScore[i]
            rsum = rsum + cardScore[rindex]
            rindex = rindex - 1

            maxsum = max(maxsum, lsum + rsum)

        # print("maxsum: ", maxsum)

        return maxsum
    
if __name__ == "__main__":
    cardScore = [1, 2, 3, 4, 5, 6]
    k = 3
    solution = Solution()
    max_score = solution.maxScore(cardScore, k)
    print("Max score that can be obtained is: ", max_score)