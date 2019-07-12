
import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    res = 'Yes'
    start = 0
    end = len(note)-1
    while start<=end:
        if start==end:
            if note[start] not in magazine:
                res ='No'
                break
        else:
            if note[start] in magazine:
				magazine.remove(note[start])
            else:
                res = 'No'
                break
			if note[end] in magazine:
				magazine.remove(note[end])
			else:
				res = 'No'
				break
        start +=1
        end -=1

    print(res)


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
