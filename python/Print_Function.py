# Problem Description:
# The included code stub will read an integer n from STDIN.
# Without using any string methods, your task is to print all integers from 1 to n (inclusive)
# on a single line, without any spaces between them.
#
# Example:
# If the input is 3, the output should be:
# 123
#
# Input Format:
# A single integer n (1 <= n <= 150)
#
# Constraints:
# 1 <= n <= 150
#
# Output Format:
# Print the numbers from 1 to n as a single string without using any string methods
# (like str(), join(), or similar). The numbers must appear consecutively without spaces.
#
# Sample Input 0:
# 3
#
# Sample Output 0:
# 123

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        print(i, end='')
