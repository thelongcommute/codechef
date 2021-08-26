# codechef.com/problems/TREEROOT

T = int(input())
for _ in range(T):
    N = int(input())
    sum_of_sums = 0
    sum_of_ids = 0
    for _ in range(N):
        tmp = [int(x) for x in input().split(" ")]
        sum_of_sums += tmp[0]
        sum_of_ids += tmp[1]
    print(sum_of_sums - sum_of_ids)
