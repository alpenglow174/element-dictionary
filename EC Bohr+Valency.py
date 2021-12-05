atomic_num = int(input("enter Z"))

# Find EC in Bohr model (KLMN)
K, L, M, N, O, P, Q, R = 0, 0, 0, 0, 0, 0, 0, 0
EC_var = atomic_num

# 2,8,8,16,16,32
# Cr, Cu, Nb, Pd, Ce, Ce, Tb, Pa, Bk
# 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, 7s, 5f, 6d, 7p, 8s, 5g, 6f, 7d, 8p, and 9s

while EC_var > 0: #Transition elements valency
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
    elif N+1 < 3:
        # fill 2 in N
        N += 1
        EC_var -= 1
# Now we are filling based on Quantum Model
    elif M+1 < 19:
        # fill 18 in M
        M += 1
        EC_var -= 1
    elif N+1 < 9:
        # fill 8 in N
        N += 1
        EC_var -= 1
    elif O+1 < 3:
        # fill 2 in O
        O += 1
        EC_var -= 1
    elif N+1 < 19:
        # fill 18 in N
        N += 1
        EC_var -= 1
    elif O+1 < 9:
        # fill 8 in O
        O += 1
        EC_var -= 1
    elif P+1 < 3:
        # fill 2 in P
        P += 1
        EC_var -= 1
    elif N+1 < 33:
        # fill 32 in N
        N += 1
        EC_var -= 1
    elif O+1 < 19:
        # fill 18 in O
        O += 1
        EC_var -= 1
    elif P+1 < 9:
        # fill 8 in P
        P += 1
        EC_var -= 1
    elif Q+1 < 3:
        # fill 2 in Q
        Q += 1
        EC_var -= 1
    elif O+1 < 33:
        # fill 32 in O
        O += 1
        EC_var -= 1
    elif P+1 < 19:
        # fill 18 in P
        P += 1
        EC_var -= 1   
    elif Q+1 < 9:
        # fill 8 in Q
        Q += 1
        EC_var -= 1
    elif R+1 < 3:
        # fill 2 in R
        R += 1
        EC_var -= 1
    elif O+1 < 51:
        # fill 50 in O
        O += 1
        EC_var -= 1
    elif P+1 < 33:
        # fill 32 in P
        P += 1
        EC_var -= 1  
    elif Q+1 < 19:
        # fill 18 in Q
        Q += 1
        EC_var -= 1
    elif R+1 < 9:
        # fill 8 in R
        R += 1
        EC_var -= 1
    

print(K, L, M, N)

'''
valency
'''
'''valency = 0
valence_e = 0

# setting no of valence electrons
if N > 0:
    # no of valence electrons is no of electrons is N
    valence_e = N
elif M > 0:
    valence_e = M
elif L > 0:
    valence_e = L
elif K > 0:
    valence_e = K

 finding valency
if valence_e <= 4:
    valency = valence_e
elif valence_e > 4 and valence_e < 9:
    valency = 8 - valence_e

print(valency)'''
