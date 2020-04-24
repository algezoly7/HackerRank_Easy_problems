#for more informations visti https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

import os

def divisibleSumPairs(n, k, ar):
    counter = 0

    for i in range(n):

        for j in range(i + 1, n):

            if((ar[i] + ar[j]) % k == 0):
                counter += 1

    return(counter)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
