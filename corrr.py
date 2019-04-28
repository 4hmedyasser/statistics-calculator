import math
from builtins import print

def getrelation(corr):
    if corr >=(-0.3) and corr<(0):
        print("negative weak correlation")
    elif corr<(-0.3) and corr>=(-0.6):
        print("negative moderate correlation")
    elif corr<(-0.6) and corr>=(-0.9):
        print("negative strong correlation")
    elif corr<(1) and corr>=(0.7):
            print("positive strong correlation")
    elif corr<(0.7) and corr>=(0.4):
        print("positive moderate correlation")
    elif corr<(0.4) and corr>=(0.1):
        print("positive weak correlation")
    else:
        print(" perfect correlation")

def correlationCoefficient(X, Y, n):
    sum_X = 0
    sum_Y = 0
    sum_XY = 0
    squareSum_X = 0
    squareSum_Y = 0
    i = 0
    while i < n:
        # sum of elements of array X.
        sum_X = sum_X + X[i]
        # sum of elements of array Y.
        sum_Y = sum_Y + Y[i]
        # sum of X[i] * Y[i].
        sum_XY = sum_XY + X[i] * Y[i]
        # sum of square of array elements.
        squareSum_X = squareSum_X + X[i] * X[i]
        squareSum_Y = squareSum_Y + Y[i] * Y[i]
        i = i + 1
    # use formula for calculating correlation
    # coefficient .
    corr = (float)(n * sum_XY - sum_X * sum_Y) /(float)(math.sqrt((n * squareSum_X-sum_X * sum_X)* (n * squareSum_Y -sum_Y * sum_Y)))
    return corr

# Driver function
X = [95,85,80,70,60]
Y = [85,95,70,65,70]
# Find the size of array.
n = len(X)
# Function call to correlationCoefficient.
print('{0:.6f}'.format(correlationCoefficient(X, Y, n)))
getrelation(correlationCoefficient(X, Y, n))
