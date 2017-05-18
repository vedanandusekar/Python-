y = input()
z= list(y)
a = len(z)-1
x= 0
for i in range (len(z)/2):
    x = z[i]
    z[i] = z[a-i]
    z[a-i] = x
print "".join(z)
 

