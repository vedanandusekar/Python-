z = input()
#z = list(y)
a = []
for i in range (len(z)):
    if z[i] not in a:
        a.append(z[i])
    else:
        continue
print a
