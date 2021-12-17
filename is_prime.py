num=int(input())
if num==1:
    print("no")
elif num==2:
    print("yes")
else:
    a=False
    for i in range(2,num):
        if num%i==0:
            a=True
            print("no")
            break
    if a==False:
        print("yes")
