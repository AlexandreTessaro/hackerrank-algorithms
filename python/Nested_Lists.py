# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.


# Enter your code here. Read input from STDIN. Print output to STDOUT

def sort_students(names_scores):
    scores = []
    for student in names_scores:
        scores.append(student[1])
        
    sorted_scores = sorted(set(scores))
    second_lowest = sorted_scores[1]
    
    names_second_lowest = []
    for student in names_scores: 
        if student[1] == second_lowest:
            names_second_lowest.append(student[0])
    names_second_lowest = sorted(names_second_lowest)
    
    for name in names_second_lowest:
        print(name)

if __name__ == '__main__':
    names_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append([name, score])
    
    sort_students(names_scores)
        