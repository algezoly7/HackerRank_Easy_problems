#for more informations visit https://www.hackerrank.com/challenges/the-birthday-bar/problem

import os

def birthday(s, d, m):
    counter = 0

    for i in range(n):
        integers_number = 0

        integersSum = 0

        while(integers_number<m):
            integersSum += s[i + integers_number]

            integers_number += 1

        if(integersSum == d):
            counter += 1

        if(integers_number + i == n):
            break
    return(counter)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()