#for more informations visit https://www.hackerrank.com/challenges/sock-merchant/problem

import os

def sockMerchant(n, ar):

    pairs_num = 0
    ar.sort()
    # the '#' is
    ar.append("#")
    i = 0
    
    while(i<n):
        if(ar[i] == ar[i+1]):
            pairs_num += 1
            i += 2

        else:
            i += 1

    return(pairs_num)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
