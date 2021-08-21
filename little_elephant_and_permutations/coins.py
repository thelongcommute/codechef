# https://www.codechef.com/problems/COINS

# The crux here was that I had to add some sort of "memory" management in order to
# remember the value of coins that we already Bytelandian coins that were already USD
# optimized so that you would not recompute them every time

def b_bank(n):
    n_2 = n // 2
    n_3 = n // 3
    n_4 = n // 4

    if n in opt_lookup:
        return opt_lookup[n]
        return upnode_max

    upnode_max = max(n, n_2 + n_3 + n_4)
    if upnode_max != n:
        upnode_max = b_bank(n_2) + b_bank(n_3) + b_bank(n_4)
        opt_lookup[n] = upnode_max
    return upnode_max


opt_lookup = {}
while True:
    try:
        n_0 = int(input())
    except:
        break

    if n_0 < n_0 // 2 + n_0 // 3 + n_0 // 4:
        max_usd = b_bank(n_0 // 2) + b_bank(n_0 // 3) + b_bank(n_0 // 4)
    else:
        max_usd = n_0

    print(max_usd)
