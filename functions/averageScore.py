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
 
n1 = int(input('Put a score: '))
n2 = int(input('Put a score: '))
n3 = int(input('Put a score: '))
n4 = int(input('Put a score: '))
n5 = int(input('Put the last score: '))
 
scores = [n1, n2, n3, n4, n5]
average_score = get_average_score(scores)
 
print('the average score is: ',average_score)
