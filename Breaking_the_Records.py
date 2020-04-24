#for more informations visit https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

import os
def breakingRecords(scores):

    highest_score = scores[0]

    highest_score_meter = 0

    for i in range(1, n):

        if(scores[i] > highest_score):
            highest_score = scores[i]

            highest_score_meter = highest_score_meter + 1

    lowest_score = scores[0]

    lowest_score_meter = 0

    for i in range(1, n):

        if(scores[i] < lowest_score):
            lowest_score = scores[i]

            lowest_score_meter = lowest_score_meter + 1

    return(highest_score_meter, lowest_score_meter)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()