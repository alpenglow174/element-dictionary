atomic_num = int(input("enter Z"))

# Find EC in Bohr model (KLMN)
K, L, M, N = 0, 0, 0, 0
EC_var = atomic_num

# 2,8,8,16,16,32

while EC_var > 0:
    if K+1 < 3:  # +1 because base is 0 and it will run 3 times otherwise
        # fill 2 in K
        K += 1
        EC_var -= 1
    elif L+1 < 9:
        # fill 8 in L
        L += 1
        EC_var -= 1
    elif M+1 < 9:
        # fill 8 in M
        M += 1
        EC_var -= 1
    elif N+1 < 17:
        # fill 16 in N
        N += 1
        EC_var -= 1


print(K, L, M, N)
