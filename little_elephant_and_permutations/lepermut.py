# https://www.codechef.com/problems/LEPERMUT

T = int(input())
for _ in range(T):
    size = int(input())
    A = [int(x) for x in input().split(" ")]
    good = "YES"
    for i in range(size):
        for j in range(i + 1, size):
            if (A[i] > A[j]) and (j - i) != 1:  # if there is an inversion and the inversion is not local
                good = "NO"
                break
    print(good)
