try:
    z=int(input())
    if z>=1:
        if z%2==0:
            print "number is even"
        else:
            print "number is odd"
    else:
            print "Plese enter valid number"
except ValueError:
    print "Oops!  That was no valid number.  Try again..."
    
