#!/usr/bin/pyhton3
# find the average score and return it
def get_average_score(scores):
    
    # compute sum of scores
    total = sum(scores) 
 
    # get the number of subjects
    count = len(scores)
    
    # compute average score
    average_score = total / count
    
    return average_score

def compute_grade(average_score):
    if average_score >= 80.0:
        grade = 'A'
    elif average_score >= 60.0:
        grade = 'B'
    elif average_score >= 50.0:
        grade = 'C'
    else:
        grade = 'F'
    
    return grade

n1 = int(input('Put a score: '))
n2 = int(input('Put a score: '))
n3 = int(input('Put a score: '))
n4 = int(input('Put a score: '))
n5 = int(input('Put the last score: '))
 
students_scores = [n1, n2, n3, n4, n5]
average_score = get_average_score(students_scores)
 
grade = compute_grade(average_score)
 
print('Average score is',  average_score)
print('Grade:', grade)


