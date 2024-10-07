n = int(input())
str=""
for i in range(1,n+1):
    if(i%2==0 or i%3==0 ):
        str+="1"
    else:
        str+="0"
    str+=" "
print(str)