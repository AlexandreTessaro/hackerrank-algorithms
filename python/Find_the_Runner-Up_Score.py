# Problem:
# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.
# The runner-up score is the second highest score in the list (not equal to the highest).
#
# Input Format:
# - The first line contains an integer n, the number of scores.
# - The second line contains n space-separated integers representing the scores.
#
# Constraints:
# - 2 <= n <= 10
# - -100 <= A[i] <= 100 (where A[i] is each score in the list)
#
# Output Format:
# Print the runner-up score (the second highest unique score).
#
# Sample Input:
# 5
# 2 3 6 6 5
#
# Sample Output:
# 5
#
# Explanation:
# The highest score is 6, but since it appears twice, the second highest unique score is 5.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    scores = list(arr)
    
    scores.sort()
    
    first, second = -100, -100
    
    for score in scores:
        if first < score:
            second = first 
            first = score
            
    print(second)
    
    
        
