s = input()
l= s.split(',')
for i in l:
    i=int(i)
    if i%2==0:
        print(str(i)+ " is even number")
    else:
        print(str(i)+ " is odd number")
