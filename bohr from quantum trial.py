ec='1s^2-2s^2-2p^6-3s^2-3p^6-4s^2-3d^10-4p^3'
count=len(ec)
ec_reverse= ec[::-1]
ec_new=''
count=0
for i in ec_reverse:
    print (i, end='')

no_of_electrons = 0
shell_number = 0
x=0

for i in ec_reverse:
    while i.isdigit() == True:
        x+=1
        c+=1
        if x == 1: #ones place
            no_of_electrons += int(i)
        elif x == 2:
            no_of_electrons += int(i) * 10
    x=0
    ec_new=ec_reverse[:c+1]

print (no_of_electrons)
