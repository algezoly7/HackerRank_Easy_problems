#for more informations vist https://www.hackerrank.com/challenges/migratory-birds/problem

import os

def migratoryBirds(arr):
    bird_frequency = [0, 0, 0, 0, 0, 0]

    for i in range(arr_count):
        bird_frequency[arr[i]] += 1

    return(bird_frequency.index(max(bird_frequency)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()