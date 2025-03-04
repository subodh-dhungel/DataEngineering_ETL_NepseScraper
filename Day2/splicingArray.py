original_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a = [[], [], [], []]

jj = 0
kk = 4
for i in range(4):
    a[i] = original_list[jj:4*(i+1)]  
    jj += 4 

print(a)