n=int(input("enter the num:"))
temp1=n
temp2=n
c=0
arm=0
while temp1:
    temp1//=10
    c+=1
while temp2:
    d=temp2%10
    arm=arm+d**c
    temp2=temp2//10
if arm==n:
    print("ARMSTRONG")
else:
    print("not an armstrong")
