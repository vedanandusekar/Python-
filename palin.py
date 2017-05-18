z = input()
x = len(z)-1

flag = 0 
for i in range(len(z)/2):
    if z[i] == z[x-i]:
        flag = 1
	#print "xyz"
    else:
        flag = 0
#print "xyz"
if flag == 1:
	print "string is palindrom"
else:
	print "string is not palindrom"
